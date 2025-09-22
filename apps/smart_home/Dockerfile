# Build stage
FROM golang:1.22-alpine AS builder

# Set working directory
WORKDIR /app
RUN apk --no-cache add ca-certificates
RUN apk --no-cache add ca-certificates git && update-ca-certificates
# Copy go.mod and go.sum files
COPY go.mod go.sum ./

RUN git config --global http.sslVerify false

ENV GOPROXY=direct
RUN git config --global http.sslVerify false
ENV GOINSECURE=golang.org,x/crypto,google.golang.org,github.com,gopkg.in
RUN go env -w GOPROXY=direct
RUN go mod download

# Copy the source code
COPY . .

# Build the application
RUN CGO_ENABLED=0 GOOS=linux go build -o smarthome

# Runtime stage
FROM alpine:latest

# Install necessary runtime dependencies
RUN apk --no-cache add ca-certificates tzdata

# Set working directory
WORKDIR /app

# Copy the binary from the builder stage
COPY --from=builder /app/smarthome .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["./smarthome"]