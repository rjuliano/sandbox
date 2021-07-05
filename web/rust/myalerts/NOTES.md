# Android

```ini
# This should be in the ~/.cargo/config file. Create one if it doesn't exist.
[target.aarch64-linux-android]
ar = "Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android30-ar"
linker = "Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android30-clang"

[target.armv7-linux-androideabi]
ar = "Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/armv7a-linux-androideabi30-ar"
linker = "Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/armv7a-linux-androideabi30-clang"

[target.i686-linux-android]
ar = "Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/i686-linux-android30-ar"
linker = "Library/Android/sdk/ndk-bundle/toolchains/llvm/prebuilt/darwin-x86_64/bin/i686-linux-android30-clang"
```