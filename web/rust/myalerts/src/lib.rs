pub fn common() -> String {
    return "Testing common function".to_string();
}

#[cfg(target_arch = "wasm32")]
pub mod wasm {
    use wasm_bindgen::prelude::*;

    #[wasm_bindgen]
    extern {
        pub fn alert(s: &str);
    }

    #[wasm_bindgen]
    pub fn greet(name: &str) {
        alert(&format!("Hello, {}!", name));
    }
}


#[cfg(target_os="android")]
pub mod android {
    use std::os::raw::{c_char};
    use std::ffi::{CString, CStr};

    #[no_mangle]
    pub extern fn rust_greeting(to: *const c_char) -> *mut c_char {
        let c_str = unsafe { CStr::from_ptr(to) };
        let recipient = match c_str.to_str() {
            Err(_) => "there",
            Ok(string) => string,
        };

        CString::new("Hello ".to_owned() + recipient).unwrap().into_raw()
    }
}
