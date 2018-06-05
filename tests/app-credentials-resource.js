const { request, prepareService, describeService, mockService, auth, assert, chance } = require('smp-test-utils');

const serviceUrl = '/app-credentials/v1/';
const medium = 'vk', mediumClientUrl = '/client-vk/v1/';
const appsClientUrl = '/apps/v1/';

describe(serviceUrl, () => {
    let smpAppId = auth.randomAppId(),
        testObject;
    beforeEach(() => auth.mock({appId: smpAppId}));
    beforeEach(() => prepareService(serviceUrl));

    describe('/', () => {
        let externalId = chance.word(),
            appId = chance.id(),
            data = {
                'medium': medium, 
                'scope': 'group', 
                'key': chance.string(), 
                'secret': chance.string(),
            },
            appFields = [
                'id',
                'app_id',
                'medium',
                'key',
                'secret',
                'scope',
                'extra',
                'created_at',
                'updated_at',
            ];
        
        describe('POST /', () => {
            it('create an app credential if data is valid', async () => {
                let sMediumClient = mockService(mediumClientUrl),
                    sAppsClient = mockService(appsClientUrl);
        
                sMediumClient.router.post('/get-app-using-app-credential', async ctx => {
                    assert.include(ctx.request.body.credential, data, 'uses provided credential data for requests');
                    ctx.status = 200;
                    ctx.body = {
                        'external_id': externalId,
                    };
                });
                
                sAppsClient.router.patch(`/by-external-id/${medium}:${externalId}`, async ctx => {
                    assert.equal(ctx.request.body.external_id, externalId, 'uses provided external_id for requests');
                    ctx.status = 200;
                    ctx.body = {
                        'id': appId,
                    }
                });

                testObject = await request.post(serviceUrl)
                    .send(data)
                    .expect(201)
                    .then(res => res.body);

                assert.equal(testObject.app_id, appId, 'app_id is set')
                assert.notEqual(testObject.id, null, 'object is saved')
                assert.include(testObject, data, 'include request data');
                assert.hasAllKeys(testObject, appFields, 'response has all keys');
            });
        });

        describe('GET /', () => {
            it('returns a list of app credential objects', async () => {
                let objects = await request.get(serviceUrl)
                    .expect(200)
                    .then(res => res.body.results);

                assert.isArray(objects, 'response is array');
                assert.isNotEmpty(objects, 'response is not empty');
                assert.deepEqual(testObject, objects[0], 'include request data');
            });
        });

        describe('GET /:id', () => {
            it('return object by id', async () => {
                let object = await request.get(`${serviceUrl}${testObject.id}`)
                    .expect(200)
                    .then(res => res.body);
                
                assert.deepEqual(testObject, object, 'include request data');    
            });
        });

        describe('PATCH /:id', () => {
            it('returns the object by id updated with data', async () => {
                let sMediumClient = mockService(mediumClientUrl),
                    sAppsClient = mockService(appsClientUrl),
                    secret = chance.string();

                data['secret'] = secret;
                
                sAppsClient.router.get(`/by-id/${testObject.app_id}`, async ctx => {
                    assert.equal(ctx.request.body.credential.id, testObject.id, 'uses provided id for requests');
                    ctx.status = 200;
                    ctx.body = {
                        'id': testObject.app_id,
                    }
                });

                sMediumClient.router.post('/get-app-using-app-credential', async ctx => {
                    assert.include(ctx.request.body.credential, data, 'uses provided credential data for requests');
                    ctx.status = 200;
                    ctx.body = {
                        'external_id': externalId,
                    };
                });

                sAppsClient.router.patch(`/by-external-id/${medium}:${externalId}`, async ctx => {
                    assert.equal(ctx.request.body.external_id, externalId, 'uses provided external_id for requests');
                    ctx.status = 200;
                    ctx.body = {
                        'id': appId,
                    }
                });

                let object = await request.patch(`${serviceUrl}${testObject.id}`)
                    .send({secret: secret})
                    .expect(200)
                    .then(res => res.body);
                
                testObject = object;
                assert.equal(testObject.secret, secret, 'secret was changed');
                assert.hasAllKeys(testObject, appFields, 'response has all keys');
            });
        });

        describe('DELETE /:id', () => {
            it('delete object by id', async () => {
                await request.delete(`${serviceUrl}${testObject.id}`)
                    .expect(204);
                
                await request.get(`${serviceUrl}${testObject.id}`)
                    .expect(404);

                let objects = await request.get(`${serviceUrl}`)
                    .expect(200)
                    .then(res => res.body.results);

                assert.isEmpty(objects, 'response is empty')
            }); 
        });
    });
});
