# Builder stage
FROM alpine:3.21 AS builder

RUN apk add --no-cache build-base wget perl
WORKDIR /opt
RUN wget https://github.com/cowsay-org/cowsay/archive/refs/tags/v3.8.3.tar.gz \
    && tar xzf v3.8.3.tar.gz \
    && cd cowsay-3.8.3 \
    && make install PREFIX=/usr/local \
    && cd / && rm -rf /opt/*

# Runtime stage
FROM alpine:3.21

# Install runtime dependencies: nc, fortune, perl (for cowsay)
RUN apk add --no-cache netcat-openbsd fortune perl

# Copy cowsay binary and share files from builder
COPY --from=builder /usr/local/bin/cowsay /usr/local/bin/cowsay
COPY --from=builder /usr/local/share/cowsay /usr/local/share/cowsay

WORKDIR /app
COPY wisecow.sh .
RUN chmod +x wisecow.sh

EXPOSE 4499
CMD ["./wisecow.sh"]
