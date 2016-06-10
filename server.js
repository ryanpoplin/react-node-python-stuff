'use strict';

const Hapi = require('hapi'),
      r = require('superagent');

const server = new Hapi.Server();
server.connection({ port: 3000 });

server.route({
    method: 'GET',
    path: '/',
    handler: function (request, reply) {
      r.get('').end((err, resp) => {
        reply(resp.text);
      });
    }
});

server.start((err) => {
    if (err) {
        throw err;
    }
    console.log('Server running at:', server.info.uri);
});
