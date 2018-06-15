const { request, prepareService, mockService, auth, assert, chance } = require('smp-test-utils');


describe('/app-credentials/v1/', () => {
    beforeEach(() => auth.mock());
    beforeEach(() => prepareService('/app-credentials/v1/'));

    describe('GET /swagger.json', () => {
        it('returns OpenAPI service specification', async () => {
            let spec = await request.get('/app-credentials/v1/swagger.json')
                .expect(200)
                .then(res => res.body);

            assert.oneOf(spec.swagger, ['2.0', '3.0']);
        });
    });
});
