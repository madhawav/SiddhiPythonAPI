
/**
 * Created by madhawa on 5/29/17.
 */

package org.wso2.siddhi.pythonapi.threadfix;

public class PyThreadFix {
    static {
        System.out.println(System.getProperty("java.library.path"));
        //System.load("/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/libpython3.5m.so");
        //System.load("/usr/lib/x86_64-linux-gnu/libboost_python-py35.so");
        System.loadLibrary("org_wso2_siddhi_pythonapi_threadfix_pythreadfix"); // Load native library at runtime
        // hello.dll (Windows) or libhello.so (Unixes)
    }

    // Declare a native method sayHello() that receives nothing and returns void
    private native void fixThread();

    public void fix(){
        fixThread();
    }
    // Test Driver
    public static void main(String[] args) {
        new PyThreadFix().fixThread();  // invoke the native method
    }
}