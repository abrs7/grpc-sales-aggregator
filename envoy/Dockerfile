# Use the full Envoy distribution which includes HTTP filters (grpc_web)
FROM envoyproxy/envoy:v1.31-latest
# Copy envoy config from the build context (docker-compose builds with context ./envoy)
# so refer to the file relative to that context
COPY envoy.yaml /etc/envoy/envoy.yaml
EXPOSE 8081
# The base image already sets /usr/local/bin/envoy as ENTRYPOINT, so provide
# only the args here (otherwise envoy will receive its own path as first arg).
CMD ["-c", "/etc/envoy/envoy.yaml", "-l", "info"]
