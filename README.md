How Allen likes to develop python apps (offer improvements please)
-

### Build your app's production image
`$ docker-compose build`

### Build your app's development image
`$ docker-compose -f docker-compose.yml -f docker-compose.dev.yml build`

### Get in a shell in your app development container
`$ ./interact.sh`

### Perpetually run tests with `ptw`
