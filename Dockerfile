FROM --platform=linux/arm64 six8/pyinstaller-alpine as builder
RUN mkdir /build
COPY ./hello.py /build/
WORKDIR /build
RUN pyinstaller --noconfirm --onefile --clean hello.py

FROM alpine as release
COPY --from=builder /build/dist/hello /usr/bin/hello
ENTRYPOINT ["hello"]