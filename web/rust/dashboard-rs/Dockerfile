FROM rust:1.53

RUN set -eux; \
    rustup --version; \
    cargo --version; \
    rustc --version; \
    rustup target add wasm32-unknown-unknown; \
    cargo install --locked trunk; \
    cargo install wasm-bindgen-cli;

