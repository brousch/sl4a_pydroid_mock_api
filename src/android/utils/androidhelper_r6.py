# androidhelper_r6.py - for SL4A R6, created on 13-Jul-2012
#
# To simplify development of SL4A Python scripts in IDEs by enabling hints &
# autocompletion through a helper class defining API functions containing
# help text in DocStrings
#
# To use, copy androidhelper_r6.py to your script's folder and import it as below
# try:
#     import androidhelper_r6 as android
# except:
#     import android
#
# Generated using AndroidHelperPyGenerator.java
# Licensed under Apache License, Ver. 2.0, http://www.apache.org/licenses/LICENSE-2.0

import android

class Android(android.Android):

    #******** ActivityResultFacade Functions : min SDK 3 ********

    def setResultBoolean(self,resultCode,resultValue):
        '''
        setResultBoolean(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Boolean resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultBoolean",resultCode,resultValue)

    def setResultBooleanArray(self,resultCode,resultValue):
        '''
        setResultBooleanArray(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Boolean[] resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultBooleanArray",resultCode,resultValue)

    def setResultByte(self,resultCode,resultValue):
        '''
        setResultByte(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Byte resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultByte",resultCode,resultValue)

    def setResultByteArray(self,resultCode,resultValue):
        '''
        setResultByteArray(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Byte[] resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultByteArray",resultCode,resultValue)

    def setResultChar(self,resultCode,resultValue):
        '''
        setResultChar(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Character resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultChar",resultCode,resultValue)

    def setResultCharArray(self,resultCode,resultValue):
        '''
        setResultCharArray(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Character[] resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultCharArray",resultCode,resultValue)

    def setResultDouble(self,resultCode,resultValue):
        '''
        setResultDouble(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Double resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultDouble",resultCode,resultValue)

    def setResultDoubleArray(self,resultCode,resultValue):
        '''
        setResultDoubleArray(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Double[] resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultDoubleArray",resultCode,resultValue)

    def setResultFloat(self,resultCode,resultValue):
        '''
        setResultFloat(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Float resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultFloat",resultCode,resultValue)

    def setResultFloatArray(self,resultCode,resultValue):
        '''
        setResultFloatArray(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Float[] resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultFloatArray",resultCode,resultValue)

    def setResultInteger(self,resultCode,resultValue):
        '''
        setResultInteger(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Integer resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultInteger",resultCode,resultValue)

    def setResultIntegerArray(self,resultCode,resultValue):
        '''
        setResultIntegerArray(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Integer[] resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultIntegerArray",resultCode,resultValue)

    def setResultLong(self,resultCode,resultValue):
        '''
        setResultLong(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Long resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultLong",resultCode,resultValue)

    def setResultLongArray(self,resultCode,resultValue):
        '''
        setResultLongArray(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Long[] resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultLongArray",resultCode,resultValue)

    def setResultSerializable(self,resultCode,resultValue):
        '''
        setResultSerializable(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Serializable resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultSerializable",resultCode,resultValue)

    def setResultShort(self,resultCode,resultValue):
        '''
        setResultShort(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Short resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultShort",resultCode,resultValue)

    def setResultShortArray(self,resultCode,resultValue):
        '''
        setResultShortArray(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          Short[] resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultShortArray",resultCode,resultValue)

    def setResultString(self,resultCode,resultValue):
        '''
        setResultString(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          String resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultString",resultCode,resultValue)

    def setResultStringArray(self,resultCode,resultValue):
        '''
        setResultStringArray(
          Integer resultCode: The result code to propagate back to the originating activity, often RESULT_CANCELED (0) or RESULT_OK (-1),
          String[] resultValue)

        Sets the result of a script execution. Whenever the script APK is called via startActivityForResult(), the resulting intent will contain SCRIPT_RESULT extra with the given value.
        '''
        return self._rpc("setResultStringArray",resultCode,resultValue)


    #******** AndroidFacade Functions : min SDK 3 ********

    def environment(self):
        '''
        environment()

        A map of various useful environment details
        '''
        return self._rpc("environment")

    def getClipboard(self):
        '''
        getClipboard()

        Read text from the clipboard.

        Returns:
          The text in the clipboard.
        '''
        return self._rpc("getClipboard")

    def getConstants(self,classname):
        '''
        getConstants(
          String classname: Class to get constants from)

        Get list of constants (static final fields) for a class
        '''
        return self._rpc("getConstants",classname)

    def getInput(self,title,message):
        '''
        getInput(
          String title[optional, default SL4A Input]: title of the input box,
          String message[optional, default Please enter value:]: message to display above the input box)

        Queries the user for a text input.

        Deprecated in r3! Please use dialogGetInput instead.
        '''
        return self._rpc("getInput",title,message)

    def getIntent(self):
        '''
        getIntent()

        Returns the intent that launched the script.
        '''
        return self._rpc("getIntent")

    def getPackageVersion(self,packageName):
        '''
        getPackageVersion(
          String packageName)

        Returns package version name.
        '''
        return self._rpc("getPackageVersion",packageName)

    def getPackageVersionCode(self,packageName):
        '''
        getPackageVersionCode(
          String packageName)

        Returns package version code.
        '''
        return self._rpc("getPackageVersionCode",packageName)

    def getPassword(self,title,message):
        '''
        getPassword(
          String title[optional, default SL4A Password Input]: title of the input box,
          String message[optional, default Please enter password:]: message to display above the input box)

        Queries the user for a password.

        Deprecated in r3! Please use dialogGetPassword instead.
        '''
        return self._rpc("getPassword",title,message)

    def log(self,message):
        '''
        log(
          String message)

        Writes message to logcat.
        '''
        return self._rpc("log",message)

    def makeIntent(self,action,uri,type,extras,categories,packagename,classname,flags):
        '''
        makeIntent(
          String action,
          String uri[optional],
          String type[optional]: MIME type/subtype of the URI,
          JSONObject extras[optional]: a Map of extras to add to the Intent,
          JSONArray categories[optional]: a List of categories to add to the Intent,
          String packagename[optional]: name of package. If used, requires classname to be useful,
          String classname[optional]: name of class. If used, requires packagename to be useful,
          Integer flags[optional]: Intent flags)

        Create an Intent.

        Returns:
          An object representing an Intent
        '''
        return self._rpc("makeIntent",action,uri,type,extras,categories,packagename,classname,flags)

    def makeToast(self,message):
        '''
        makeToast(
          String message)

        Displays a short-duration Toast notification.
        '''
        return self._rpc("makeToast",message)

    def notify(self,title,message):
        '''
        notify(
          String title: title,
          String message)

        Displays a notification that will be canceled when the user clicks on it.
        '''
        return self._rpc("notify",title,message)

    def requiredVersion(self,requiredVersion):
        '''
        requiredVersion(
          Integer requiredVersion)

        Checks if version of SL4A is greater than or equal to the specified version.
        '''
        return self._rpc("requiredVersion",requiredVersion)

    def sendBroadcast(self,action,uri,type,extras,packagename,classname):
        '''
        sendBroadcast(
          String action,
          String uri[optional],
          String type[optional]: MIME type/subtype of the URI,
          JSONObject extras[optional]: a Map of extras to add to the Intent,
          String packagename[optional]: name of package. If used, requires classname to be useful,
          String classname[optional]: name of class. If used, requires packagename to be useful)

        Send a broadcast.
        '''
        return self._rpc("sendBroadcast",action,uri,type,extras,packagename,classname)

    def sendBroadcastIntent(self,intent):
        '''
        sendBroadcastIntent(
          Intent intent: Intent in the format as returned from makeIntent)

        Send Broadcast Intent
        '''
        return self._rpc("sendBroadcastIntent",intent)

    def sendEmail(self,to,subject,body,attachmentUri):
        '''
        sendEmail(
          String to: A comma separated list of recipients.,
          String subject,
          String body,
          String attachmentUri[optional])

        Launches an activity that sends an e-mail message to a given recipient.
        '''
        return self._rpc("sendEmail",to,subject,body,attachmentUri)

    def setClipboard(self,text):
        '''
        setClipboard(
          String text)

        Put text in the clipboard.
        '''
        return self._rpc("setClipboard",text)

    def startActivity(self,action,uri,type,extras,wait,packagename,classname):
        '''
        startActivity(
          String action,
          String uri[optional],
          String type[optional]: MIME type/subtype of the URI,
          JSONObject extras[optional]: a Map of extras to add to the Intent,
          Boolean wait[optional]: block until the user exits the started activity,
          String packagename[optional]: name of package. If used, requires classname to be useful,
          String classname[optional]: name of class. If used, requires packagename to be useful)

        Starts an activity.
        '''
        return self._rpc("startActivity",action,uri,type,extras,wait,packagename,classname)

    def startActivityForResult(self,action,uri,type,extras,packagename,classname):
        '''
        startActivityForResult(
          String action,
          String uri[optional],
          String type[optional]: MIME type/subtype of the URI,
          JSONObject extras[optional]: a Map of extras to add to the Intent,
          String packagename[optional]: name of package. If used, requires classname to be useful,
          String classname[optional]: name of class. If used, requires packagename to be useful)

        Starts an activity and returns the result.

        Returns:
          A Map representation of the result Intent.
        '''
        return self._rpc("startActivityForResult",action,uri,type,extras,packagename,classname)

    def startActivityForResultIntent(self,intent):
        '''
        startActivityForResultIntent(
          Intent intent: Intent in the format as returned from makeIntent)

        Starts an activity and returns the result.

        Returns:
          A Map representation of the result Intent.
        '''
        return self._rpc("startActivityForResultIntent",intent)

    def startActivityIntent(self,intent,wait):
        '''
        startActivityIntent(
          Intent intent: Intent in the format as returned from makeIntent,
          Boolean wait[optional]: block until the user exits the started activity)

        Start Activity using Intent
        '''
        return self._rpc("startActivityIntent",intent,wait)

    def vibrate(self,duration):
        '''
        vibrate(
          Integer duration[optional, default 300]: duration in milliseconds)

        Vibrates the phone or a specified duration in milliseconds.
        '''
        return self._rpc("vibrate",duration)


    #******** ApplicationManagerFacade Functions : min SDK 3 ********

    def forceStopPackage(self,packageName):
        '''
        forceStopPackage(
          String packageName: name of package)

        Force stops a package.
        '''
        return self._rpc("forceStopPackage",packageName)

    def getLaunchableApplications(self):
        '''
        getLaunchableApplications()

        Returns a list of all launchable application class names.
        '''
        return self._rpc("getLaunchableApplications")

    def getRunningPackages(self):
        '''
        getRunningPackages()

        Returns a list of packages running activities or services.

        Returns:
          List of packages running activities.
        '''
        return self._rpc("getRunningPackages")

    def launch(self,className):
        '''
        launch(
          String className)

        Start activity with the given class name.
        '''
        return self._rpc("launch",className)


    #******** BatteryManagerFacade Functions : min SDK 3 ********

    def batteryCheckPresent(self):
        '''
        batteryCheckPresent()

        Returns the most recently received battery presence data.
        '''
        return self._rpc("batteryCheckPresent")

    def batteryGetHealth(self):
        '''
        batteryGetHealth()

        Returns the most recently received battery health data:
        1 - unknown;
        2 - good;
        3 - overheat;
        4 - dead;
        5 - over voltage;
        6 - unspecified failure;
        '''
        return self._rpc("batteryGetHealth")

    def batteryGetLevel(self):
        '''
        batteryGetLevel()

        Returns the most recently received battery level (percentage).
        '''
        return self._rpc("batteryGetLevel")

    def batteryGetPlugType(self):
        '''
        batteryGetPlugType()

        Returns the most recently received plug type data:
        -1 - unknown
        0 - unplugged;
        1 - power source is an AC charger
        2 - power source is a USB port
        '''
        return self._rpc("batteryGetPlugType")

    def batteryGetStatus(self):
        '''
        batteryGetStatus()

        Returns  the most recently received battery status data:
        1 - unknown;
        2 - charging;
        3 - discharging;
        4 - not charging;
        5 - full;
        '''
        return self._rpc("batteryGetStatus")

    def batteryGetTechnology(self):
        '''
        batteryGetTechnology()

        Returns the most recently received battery technology data.
        '''
        return self._rpc("batteryGetTechnology")

    def batteryGetTemperature(self):
        '''
        batteryGetTemperature()

        Returns the most recently received battery temperature.
        '''
        return self._rpc("batteryGetTemperature")

    def batteryGetVoltage(self):
        '''
        batteryGetVoltage()

        Returns the most recently received battery voltage.
        '''
        return self._rpc("batteryGetVoltage")

    def batteryStartMonitoring(self):
        '''
        batteryStartMonitoring()

        Starts tracking battery state.

        Generates "battery" events.
        '''
        return self._rpc("batteryStartMonitoring")

    def batteryStopMonitoring(self):
        '''
        batteryStopMonitoring()

        Stops tracking battery state.
        '''
        return self._rpc("batteryStopMonitoring")

    def readBatteryData(self):
        '''
        readBatteryData()

        Returns the most recently recorded battery data.
        '''
        return self._rpc("readBatteryData")


    #******** BluetoothFacade Functions : min SDK 5 ********

    def bluetoothAccept(self,uuid,timeout):
        '''
        bluetoothAccept(
          String uuid[optional, default 457807c0-4897-11df-9879-0800200c9a66],
          Integer timeout[optional, default 0]: How long to wait for a new connection, 0 is wait for ever)

        Listens for and accepts a Bluetooth connection. Blocks until the connection is established or fails.
        '''
        return self._rpc("bluetoothAccept",uuid,timeout)

    def bluetoothActiveConnections(self):
        '''
        bluetoothActiveConnections()

        Returns active Bluetooth connections.
        '''
        return self._rpc("bluetoothActiveConnections")

    def bluetoothConnect(self,uuid,address):
        '''
        bluetoothConnect(
          String uuid[optional, default 457807c0-4897-11df-9879-0800200c9a66]: The UUID passed here must match the UUID used by the server device.,
          String address[optional]: The user will be presented with a list of discovered devices to choose from if an address is not provided.)

        Connect to a device over Bluetooth. Blocks until the connection is established or fails.

        Returns:
          True if the connection was established successfully.
        '''
        return self._rpc("bluetoothConnect",uuid,address)

    def bluetoothDiscoveryCancel(self):
        '''
        bluetoothDiscoveryCancel()

        Cancel the current device discovery process.

        Returns:
          true on success, false on error
        '''
        return self._rpc("bluetoothDiscoveryCancel")

    def bluetoothDiscoveryStart(self):
        '''
        bluetoothDiscoveryStart()

        Start the remote device discovery process.

        Returns:
          true on success, false on error
        '''
        return self._rpc("bluetoothDiscoveryStart")

    def bluetoothGetConnectedDeviceName(self,connID):
        '''
        bluetoothGetConnectedDeviceName(
          String connID[optional, default null]: Connection id)

        Returns the name of the connected device.
        '''
        return self._rpc("bluetoothGetConnectedDeviceName",connID)

    def bluetoothGetLocalAddress(self):
        '''
        bluetoothGetLocalAddress()

        Returns the hardware address of the local Bluetooth adapter.
        '''
        return self._rpc("bluetoothGetLocalAddress")

    def bluetoothGetLocalName(self):
        '''
        bluetoothGetLocalName()

        Gets the Bluetooth Visible device name
        '''
        return self._rpc("bluetoothGetLocalName")

    def bluetoothGetRemoteDeviceName(self,address):
        '''
        bluetoothGetRemoteDeviceName(
          String address: Bluetooth Address For Target Device)

        Queries a remote device for it's name or null if it can't be resolved
        '''
        return self._rpc("bluetoothGetRemoteDeviceName",address)

    def bluetoothGetScanMode(self):
        '''
        bluetoothGetScanMode()

        Gets the scan mode for the local dongle.

        Return values:

        	-1 when Bluetooth is disabled.

        	0 if non discoverable and non connectable.


1 connectable non discoverable.
3 connectable and discoverable.
        '''
        return self._rpc("bluetoothGetScanMode")

    def bluetoothIsDiscovering(self):
        '''
        bluetoothIsDiscovering()

        Return true if the local Bluetooth adapter is currently in the device discovery process.
        '''
        return self._rpc("bluetoothIsDiscovering")

    def bluetoothMakeDiscoverable(self,duration):
        '''
        bluetoothMakeDiscoverable(
          Integer duration[optional, default 300]: period of time, in seconds, during which the device should be discoverable)

        Requests that the device be discoverable for Bluetooth connections.
        '''
        return self._rpc("bluetoothMakeDiscoverable",duration)

    def bluetoothRead(self,bufferSize,connID):
        '''
        bluetoothRead(
          Integer bufferSize[optional, default 4096],
          String connID[optional, default null]: Connection id)

        Read up to bufferSize ASCII characters.
        '''
        return self._rpc("bluetoothRead",bufferSize,connID)

    def bluetoothReadBinary(self,bufferSize,connID):
        '''
        bluetoothReadBinary(
          Integer bufferSize[optional, default 4096],
          String connID[optional, default ]: Connection id)

        Read up to bufferSize bytes and return a chunked, base64 encoded string.
        '''
        return self._rpc("bluetoothReadBinary",bufferSize,connID)

    def bluetoothReadLine(self,connID):
        '''
        bluetoothReadLine(
          String connID[optional, default null]: Connection id)

        Read the next line.
        '''
        return self._rpc("bluetoothReadLine",connID)

    def bluetoothReadReady(self,connID):
        '''
        bluetoothReadReady(
          String connID[optional, default ]: Connection id)

        Returns True if the next read is guaranteed not to block.
        '''
        return self._rpc("bluetoothReadReady",connID)

    def bluetoothSetLocalName(self,name):
        '''
        bluetoothSetLocalName(
          String name: New local name)

        Sets the Bluetooth Visible device name, returns True on success
        '''
        return self._rpc("bluetoothSetLocalName",name)

    def bluetoothStop(self,connID):
        '''
        bluetoothStop(
          String connID[optional, default null]: Connection id)

        Stops Bluetooth connection.
        '''
        return self._rpc("bluetoothStop",connID)

    def bluetoothWrite(self,ascii,connID):
        '''
        bluetoothWrite(
          String ascii,
          String connID[optional, default ]: Connection id)

        Sends ASCII characters over the currently open Bluetooth connection.
        '''
        return self._rpc("bluetoothWrite",ascii,connID)

    def bluetoothWriteBinary(self,base64,connID):
        '''
        bluetoothWriteBinary(
          String base64: A base64 encoded String of the bytes to be sent.,
          String connID[optional, default ]: Connection id)

        Send bytes over the currently open Bluetooth connection.
        '''
        return self._rpc("bluetoothWriteBinary",base64,connID)

    def checkBluetoothState(self):
        '''
        checkBluetoothState()

        Checks Bluetooth state.

        Returns:
          True if Bluetooth is enabled.
        '''
        return self._rpc("checkBluetoothState")

    def toggleBluetoothState(self,enabled,prompt):
        '''
        toggleBluetoothState(
          Boolean enabled[optional],
          Boolean prompt[optional, default true]: Prompt the user to confirm changing the Bluetooth state.)

        Toggle Bluetooth on and off.

        Returns:
          True if Bluetooth is enabled.
        '''
        return self._rpc("toggleBluetoothState",enabled,prompt)


    #******** CameraFacade Functions : min SDK 3 ********

    def cameraCapturePicture(self,targetPath,useAutoFocus):
        '''
        cameraCapturePicture(
          String targetPath,
          Boolean useAutoFocus[optional, default true])

        Take a picture and save it to the specified path.

        Returns:
          A map of Booleans autoFocus and takePicture where True indicates success.
        '''
        return self._rpc("cameraCapturePicture",targetPath,useAutoFocus)

    def cameraInteractiveCapturePicture(self,targetPath):
        '''
        cameraInteractiveCapturePicture(
          String targetPath)

        Starts the image capture application to take a picture and saves it to the specified path.
        '''
        return self._rpc("cameraInteractiveCapturePicture",targetPath)


    #******** CommonIntentsFacade Functions : min SDK 3 ********

    def pick(self,uri):
        '''
        pick(
          String uri)

        Display content to be picked by URI (e.g. contacts)

        Returns:
          A map of result values.
        '''
        return self._rpc("pick",uri)

    def scanBarcode(self):
        '''
        scanBarcode()

        Starts the barcode scanner.

        Returns:
          A Map representation of the result Intent.
        '''
        return self._rpc("scanBarcode")

    def search(self,query):
        '''
        search(
          String query)

        Starts a search for the given query.
        '''
        return self._rpc("search",query)

    def view(self,uri,type,extras):
        '''
        view(
          String uri,
          String type[optional]: MIME type/subtype of the URI,
          JSONObject extras[optional]: a Map of extras to add to the Intent)

        Start activity with view action by URI (i.e. browser, contacts, etc.).
        '''
        return self._rpc("view",uri,type,extras)

    def viewContacts(self):
        '''
        viewContacts()

        Opens the list of contacts.
        '''
        return self._rpc("viewContacts")

    def viewHtml(self,path):
        '''
        viewHtml(
          String path: the path to the HTML file)

        Opens the browser to display a local HTML file.
        '''
        return self._rpc("viewHtml",path)

    def viewMap(self,query):
        '''
        viewMap(
          String query, e.g. pizza, 123 My Street)

        Opens a map search for query (e.g. pizza, 123 My Street).
        '''
        return self._rpc("viewMap",query)


    #******** ContactsFacade Functions : min SDK 3 ********

    def contactsGet(self,attributes):
        '''
        contactsGet(
          JSONArray attributes[optional])

        Returns a List of all contacts.

        Returns:
          a List of contacts as Maps
        '''
        return self._rpc("contactsGet",attributes)

    def contactsGetAttributes(self):
        '''
        contactsGetAttributes()

        Returns a List of all possible attributes for contacts.
        '''
        return self._rpc("contactsGetAttributes")

    def contactsGetById(self,id,attributes):
        '''
        contactsGetById(
          Integer id,
          JSONArray attributes[optional])

        Returns contacts by ID.
        '''
        return self._rpc("contactsGetById",id,attributes)

    def contactsGetCount(self):
        '''
        contactsGetCount()

        Returns the number of contacts.
        '''
        return self._rpc("contactsGetCount")

    def contactsGetIds(self):
        '''
        contactsGetIds()

        Returns a List of all contact IDs.
        '''
        return self._rpc("contactsGetIds")

    def pickContact(self):
        '''
        pickContact()

        Displays a list of contacts to pick from.

        Returns:
          A map of result values.
        '''
        return self._rpc("pickContact")

    def pickPhone(self):
        '''
        pickPhone()

        Displays a list of phone numbers to pick from.

        Returns:
          The selected phone number.
        '''
        return self._rpc("pickPhone")

    def queryAttributes(self,uri):
        '''
        queryAttributes(
          String uri: The URI, using the content:// scheme, for the content to retrieve.)

        Content Resolver Query Attributes

        Returns:
          a list of available columns for a given content uri
        '''
        return self._rpc("queryAttributes",uri)

    def queryContent(self,uri,attributes,selection,selectionArgs,order):
        '''
        queryContent(
          String uri: The URI, using the content:// scheme, for the content to retrieve.,
          JSONArray attributes[optional]: A list of which columns to return. Passing null will return all columns,
          String selection[optional]: A filter declaring which rows to return,
          JSONArray selectionArgs[optional]: You may include ?s in selection, which will be replaced by the values from selectionArgs,
          String order[optional]: How to order the rows)

        Content Resolver Query

        Returns:
          result of query as Maps
        '''
        return self._rpc("queryContent",uri,attributes,selection,selectionArgs,order)


    #******** EventFacade Functions : min SDK 3 ********

    def eventClearBuffer(self):
        '''
        eventClearBuffer()

        Clears all events from the event buffer.
        '''
        return self._rpc("eventClearBuffer")

    def eventGetBrodcastCategories(self):
        '''
        eventGetBrodcastCategories()

        Lists all the broadcast signals we are listening for
        '''
        return self._rpc("eventGetBrodcastCategories")

    def eventPoll(self,number_of_events):
        '''
        eventPoll(
          Integer number_of_events[optional, default 1])

        Returns and removes the oldest n events (i.e. location or sensor update, etc.) from the event buffer.

        Returns:
          A List of Maps of event properties.
        '''
        return self._rpc("eventPoll",number_of_events)

    def eventPost(self,name,data,enqueue):
        '''
        eventPost(
          String name: Name of event,
          String data: Data contained in event.,
          Boolean enqueue[optional, default null]: Set to False if you don't want your events to be added to the event queue, just dispatched.)

        Post an event to the event queue.
        '''
        return self._rpc("eventPost",name,data,enqueue)

    def eventRegisterForBroadcast(self,category,enqueue):
        '''
        eventRegisterForBroadcast(
          String category,
          Boolean enqueue[optional, default true]: Should this events be added to the event queue or only dispatched)

        Registers a listener for a new broadcast signal
        '''
        return self._rpc("eventRegisterForBroadcast",category,enqueue)

    def eventUnregisterForBroadcast(self,category):
        '''
        eventUnregisterForBroadcast(
          String category)

        Stop listening for a broadcast signal
        '''
        return self._rpc("eventUnregisterForBroadcast",category)

    def eventWait(self,timeout):
        '''
        eventWait(
          Integer timeout[optional]: the maximum time to wait)

        Blocks until an event occurs. The returned event is removed from the buffer.

        Returns:
          Map of event properties.
        '''
        return self._rpc("eventWait",timeout)

    def eventWaitFor(self,eventName,timeout):
        '''
        eventWaitFor(
          String eventName,
          Integer timeout[optional]: the maximum time to wait (in ms))

        Blocks until an event with the supplied name occurs. The returned event is not removed from the buffer.

        Returns:
          Map of event properties.
        '''
        return self._rpc("eventWaitFor",eventName,timeout)

    def postEvent(self,name,data):
        '''
        rpcPostEvent(
          String name,
          String data)

        Post an event to the event queue.

        Deprecated in r4! Please use eventPost instead.
        '''
        return self._rpc("postEvent",name,data)

    def receiveEvent(self):
        '''
        receiveEvent()

        Returns and removes the oldest event (i.e. location or sensor update, etc.) from the event buffer.

        Returns:
          Map of event properties.

        Deprecated in r4! Please use eventPoll instead.
        '''
        return self._rpc("receiveEvent")

    def startEventDispatcher(self,port):
        '''
        startEventDispatcher(
          Integer port[optional, default 0]: Port to use)

        Opens up a socket where you can read for events posted
        '''
        return self._rpc("startEventDispatcher",port)

    def stopEventDispatcher(self):
        '''
        stopEventDispatcher()

        Stops the event server, you can't read in the port anymore
        '''
        return self._rpc("stopEventDispatcher")

    def waitForEvent(self,eventName,timeout):
        '''
        waitForEvent(
          String eventName,
          Integer timeout[optional]: the maximum time to wait)

        Blocks until an event with the supplied name occurs. The returned event is not removed from the buffer.

        Returns:
          Map of event properties.

        Deprecated in r4! Please use eventWaitFor instead.
        '''
        return self._rpc("waitForEvent",eventName,timeout)


    #******** LocationFacade Functions : min SDK 3 ********

    def geocode(self,latitude,longitude,maxResults):
        '''
        geocode(
          Double latitude,
          Double longitude,
          Integer maxResults[optional, default 1]: maximum number of results)

        Returns a list of addresses for the given latitude and longitude.

        Returns:
          A list of addresses.
        '''
        return self._rpc("geocode",latitude,longitude,maxResults)

    def getLastKnownLocation(self):
        '''
        getLastKnownLocation()

        Returns the last known location of the device.

        Returns:
          A map of location information by provider.
        '''
        return self._rpc("getLastKnownLocation")

    def locationProviderEnabled(self,provider):
        '''
        locationProviderEnabled(
          String provider: Name of location provider)

        Ask if provider is enabled
        '''
        return self._rpc("locationProviderEnabled",provider)

    def locationProviders(self):
        '''
        locationProviders()

        Returns availables providers on the phone
        '''
        return self._rpc("locationProviders")

    def readLocation(self):
        '''
        readLocation()

        Returns the current location as indicated by all available providers.

        Returns:
          A map of location information by provider.
        '''
        return self._rpc("readLocation")

    def startLocating(self,minDistance,minUpdateDistance):
        '''
        startLocating(
          Integer minDistance[optional, default 60000]: minimum time between updates in milliseconds,
          Integer minUpdateDistance[optional, default 30]: minimum distance between updates in meters)

        Starts collecting location data.

        Generates "location" events.
        '''
        return self._rpc("startLocating",minDistance,minUpdateDistance)

    def stopLocating(self):
        '''
        stopLocating()

        Stops collecting location data.
        '''
        return self._rpc("stopLocating")


    #******** MediaPlayerFacade Functions : min SDK 3 ********

    def mediaIsPlaying(self,tag):
        '''
        mediaIsPlaying(
          String tag[optional, default default]: string identifying resource)

        Checks if media file is playing.

        Returns:
          true if playing
        '''
        return self._rpc("mediaIsPlaying",tag)

    def mediaPlay(self,url,tag,play):
        '''
        mediaPlay(
          String url: url of media resource,
          String tag[optional, default default]: string identifying resource,
          Boolean play[optional, default true]: start playing immediately)

        Open a media file

        Returns:
          true if play successful
        '''
        return self._rpc("mediaPlay",url,tag,play)

    def mediaPlayClose(self,tag):
        '''
        mediaPlayClose(
          String tag[optional, default default]: string identifying resource)

        Close media file

        Returns:
          true if successful
        '''
        return self._rpc("mediaPlayClose",tag)

    def mediaPlayInfo(self,tag):
        '''
        mediaPlayInfo(
          String tag[optional, default default]: string identifying resource)

        Information on current media

        Returns:
          Media Information
        '''
        return self._rpc("mediaPlayInfo",tag)

    def mediaPlayList(self):
        '''
        mediaPlayList()

        Lists currently loaded media

        Returns:
          List of Media Tags
        '''
        return self._rpc("mediaPlayList")

    def mediaPlayPause(self,tag):
        '''
        mediaPlayPause(
          String tag[optional, default default]: string identifying resource)

        pause playing media file

        Returns:
          true if successful
        '''
        return self._rpc("mediaPlayPause",tag)

    def mediaPlaySeek(self,msec,tag):
        '''
        mediaPlaySeek(
          Integer msec: Position in millseconds,
          String tag[optional, default default]: string identifying resource)

        Seek To Position

        Returns:
          New Position (in ms)
        '''
        return self._rpc("mediaPlaySeek",msec,tag)

    def mediaPlaySetLooping(self,enabled,tag):
        '''
        mediaPlaySetLooping(
          Boolean enabled[optional, default true],
          String tag[optional, default default]: string identifying resource)

        Set Looping

        Returns:
          True if successful
        '''
        return self._rpc("mediaPlaySetLooping",enabled,tag)

    def mediaPlayStart(self,tag):
        '''
        mediaPlayStart(
          String tag[optional, default default]: string identifying resource)

        start playing media file

        Returns:
          true if successful
        '''
        return self._rpc("mediaPlayStart",tag)


    #******** MediaRecorderFacade Functions : min SDK 3 ********

    def recorderCaptureVideo(self,targetPath,duration,recordAudio):
        '''
        recorderCaptureVideo(
          String targetPath,
          Integer duration[optional],
          Boolean recordAudio[optional, default true])

        Records video (and optionally audio) from the camera and saves it to the given location.
        Duration specifies the maximum duration of the recording session.
        If duration is not provided this method will return immediately and the recording will only be stopped
        when recorderStop is called or when a scripts exits.
        Otherwise it will block for the time period equal to the duration argument.
        '''
        return self._rpc("recorderCaptureVideo",targetPath,duration,recordAudio)

    def recorderStartMicrophone(self,targetPath):
        '''
        recorderStartMicrophone(
          String targetPath)

        Records audio from the microphone and saves it to the given location.
        '''
        return self._rpc("recorderStartMicrophone",targetPath)

    def recorderStartVideo(self,targetPath,duration,videoSize):
        '''
        recorderStartVideo(
          String targetPath,
          Integer duration[optional, default 0],
          Integer videoSize[optional, default 1])

        Records video from the camera and saves it to the given location.
        Duration specifies the maximum duration of the recording session.
        If duration is 0 this method will return and the recording will only be stopped
        when recorderStop is called or when a scripts exits.
        Otherwise it will block for the time period equal to the duration argument.
        videoSize: 0=160x120, 1=320x240, 2=352x288, 3=640x480, 4=800x480.
        '''
        return self._rpc("recorderStartVideo",targetPath,duration,videoSize)

    def recorderStop(self):
        '''
        recorderStop()

        Stops a previously started recording.
        '''
        return self._rpc("recorderStop")

    def startInteractiveVideoRecording(self,path):
        '''
        startInteractiveVideoRecording(
          String path)

        Starts the video capture application to record a video and saves it to the specified path.
        '''
        return self._rpc("startInteractiveVideoRecording",path)


    #******** PhoneFacade Functions : min SDK 3 ********

    def checkNetworkRoaming(self):
        '''
        checkNetworkRoaming()

        Returns true if the device is considered roaming on the current network, for GSM purposes.
        '''
        return self._rpc("checkNetworkRoaming")

    def getCellLocation(self):
        '''
        getCellLocation()

        Returns the current cell location.
        '''
        return self._rpc("getCellLocation")

    def getDeviceId(self):
        '''
        getDeviceId()

        Returns the unique device ID, for example, the IMEI for GSM and the MEID for CDMA phones. Return null if device ID is not available.
        '''
        return self._rpc("getDeviceId")

    def getDeviceSoftwareVersion(self):
        '''
        getDeviceSoftwareVersion()

        Returns the software version number for the device, for example, the IMEI/SV for GSM phones. Return null if the software version is not available.
        '''
        return self._rpc("getDeviceSoftwareVersion")

    def getLine1Number(self):
        '''
        getLine1Number()

        Returns the phone number string for line 1, for example, the MSISDN for a GSM phone. Return null if it is unavailable.
        '''
        return self._rpc("getLine1Number")

    def getNeighboringCellInfo(self):
        '''
        getNeighboringCellInfo()

        Returns the neighboring cell information of the device.
        '''
        return self._rpc("getNeighboringCellInfo")

    def getNetworkOperator(self):
        '''
        getNetworkOperator()

        Returns the numeric name (MCC+MNC) of current registered operator.
        '''
        return self._rpc("getNetworkOperator")

    def getNetworkOperatorName(self):
        '''
        getNetworkOperatorName()

        Returns the alphabetic name of current registered operator.
        '''
        return self._rpc("getNetworkOperatorName")

    def getNetworkType(self):
        '''
        getNetworkType()

        Returns a the radio technology (network type) currently in use on the device.
        '''
        return self._rpc("getNetworkType")

    def getPhoneType(self):
        '''
        getPhoneType()

        Returns the device phone type.
        '''
        return self._rpc("getPhoneType")

    def getSimCountryIso(self):
        '''
        getSimCountryIso()

        Returns the ISO country code equivalent for the SIM provider's country code.
        '''
        return self._rpc("getSimCountryIso")

    def getSimOperator(self):
        '''
        getSimOperator()

        Returns the MCC+MNC (mobile country code + mobile network code) of the provider of the SIM. 5 or 6 decimal digits.
        '''
        return self._rpc("getSimOperator")

    def getSimOperatorName(self):
        '''
        getSimOperatorName()

        Returns the Service Provider Name (SPN).
        '''
        return self._rpc("getSimOperatorName")

    def getSimSerialNumber(self):
        '''
        getSimSerialNumber()

        Returns the serial number of the SIM, if applicable. Return null if it is unavailable.
        '''
        return self._rpc("getSimSerialNumber")

    def getSimState(self):
        '''
        getSimState()

        Returns the state of the device SIM card.
        '''
        return self._rpc("getSimState")

    def getSubscriberId(self):
        '''
        getSubscriberId()

        Returns the unique subscriber ID, for example, the IMSI for a GSM phone. Return null if it is unavailable.
        '''
        return self._rpc("getSubscriberId")

    def getVoiceMailAlphaTag(self):
        '''
        getVoiceMailAlphaTag()

        Retrieves the alphabetic identifier associated with the voice mail number.
        '''
        return self._rpc("getVoiceMailAlphaTag")

    def getVoiceMailNumber(self):
        '''
        getVoiceMailNumber()

        Returns the voice mail number. Return null if it is unavailable.
        '''
        return self._rpc("getVoiceMailNumber")

    def phoneCall(self,uri):
        '''
        phoneCall(
          String uri)

        Calls a contact/phone number by URI.
        '''
        return self._rpc("phoneCall",uri)

    def phoneCallNumber(self,phone):
        '''
        phoneCallNumber(
          String phone number)

        Calls a phone number.
        '''
        return self._rpc("phoneCallNumber",phone)

    def phoneDial(self,uri):
        '''
        phoneDial(
          String uri)

        Dials a contact/phone number by URI.
        '''
        return self._rpc("phoneDial",uri)

    def phoneDialNumber(self,phone):
        '''
        phoneDialNumber(
          String phone number)

        Dials a phone number.
        '''
        return self._rpc("phoneDialNumber",phone)

    def readPhoneState(self):
        '''
        readPhoneState()

        Returns the current phone state and incoming number.

        Returns:
          A Map of "state" and "incomingNumber"
        '''
        return self._rpc("readPhoneState")

    def startTrackingPhoneState(self):
        '''
        startTrackingPhoneState()

        Starts tracking phone state.

        Generates "phone" events.
        '''
        return self._rpc("startTrackingPhoneState")

    def stopTrackingPhoneState(self):
        '''
        stopTrackingPhoneState()

        Stops tracking phone state.
        '''
        return self._rpc("stopTrackingPhoneState")


    #******** PreferencesFacade Functions : min SDK 3 ********

    def prefGetAll(self,filename):
        '''
        prefGetAll(
          String filename[optional]: Desired preferences file. If not defined, uses the default Shared Preferences.)

        Get list of Shared Preference Values

        Returns:
          Map of key,value
        '''
        return self._rpc("prefGetAll",filename)

    def prefGetValue(self,key,filename):
        '''
        prefGetValue(
          String key,
          String filename[optional]: Desired preferences file. If not defined, uses the default Shared Preferences.)

        Read a value from shared preferences
        '''
        return self._rpc("prefGetValue",key,filename)

    def prefPutValue(self,key,value,filename):
        '''
        prefPutValue(
          String key,
          Object value,
          String filename[optional]: Desired preferences file. If not defined, uses the default Shared Preferences.)

        Write a value to shared preferences
        '''
        return self._rpc("prefPutValue",key,value,filename)


    #******** SensorManagerFacade Functions : min SDK 3 ********

    def readSensors(self):
        '''
        readSensors()

        Returns the most recently recorded sensor data.
        '''
        return self._rpc("readSensors")

    def sensorsGetAccuracy(self):
        '''
        sensorsGetAccuracy()

        Returns the most recently received accuracy value.
        '''
        return self._rpc("sensorsGetAccuracy")

    def sensorsGetLight(self):
        '''
        sensorsGetLight()

        Returns the most recently received light value.
        '''
        return self._rpc("sensorsGetLight")

    def sensorsReadAccelerometer(self):
        '''
        sensorsReadAccelerometer()

        Returns the most recently received accelerometer values.

        Returns:
          a List of Floats [(acceleration on the) X axis, Y axis, Z axis].
        '''
        return self._rpc("sensorsReadAccelerometer")

    def sensorsReadMagnetometer(self):
        '''
        sensorsReadMagnetometer()

        Returns the most recently received magnetic field values.

        Returns:
          a List of Floats [(magnetic field value for) X axis, Y axis, Z axis].
        '''
        return self._rpc("sensorsReadMagnetometer")

    def sensorsReadOrientation(self):
        '''
        sensorsReadOrientation()

        Returns the most recently received orientation values.

        Returns:
          a List of Doubles [azimuth, pitch, roll].
        '''
        return self._rpc("sensorsReadOrientation")

    def startSensing(self,sampleSize):
        '''
        startSensing(
          Integer sampleSize[optional, default 5]: number of samples for calculating average readings)

        Starts recording sensor data to be available for polling.

        Deprecated in 4! Please use startSensingTimed or startSensingThreshhold instead.
        '''
        return self._rpc("startSensing",sampleSize)

    def startSensingThreshold(self,sensorNumber,threshold,axis):
        '''
        startSensingThreshold(
          Integer sensorNumber: 1 = Orientation, 2 = Accelerometer, 3 = Magnetometer and 4 = Light,
          Integer threshold: Threshold level for chosen sensor (integer),
          Integer axis: 0 = No axis, 1 = X, 2 = Y, 3 = X+Y, 4 = Z, 5= X+Z, 6 = Y+Z, 7 = X+Y+Z)

        Records to the Event Queue sensor data exceeding a chosen threshold.

        Generates "threshold" events.
        '''
        return self._rpc("startSensingThreshold",sensorNumber,threshold,axis)

    def startSensingTimed(self,sensorNumber,delayTime):
        '''
        startSensingTimed(
          Integer sensorNumber: 1 = All, 2 = Accelerometer, 3 = Magnetometer and 4 = Light,
          Integer delayTime: Minimum time between readings in milliseconds)

        Starts recording sensor data to be available for polling.

        Generates "sensors" events.
        '''
        return self._rpc("startSensingTimed",sensorNumber,delayTime)

    def stopSensing(self):
        '''
        stopSensing()

        Stops collecting sensor data.
        '''
        return self._rpc("stopSensing")


    #******** SettingsFacade Functions : min SDK 3 ********

    def checkAirplaneMode(self):
        '''
        checkAirplaneMode()

        Checks the airplane mode setting.

        Returns:
          True if airplane mode is enabled.
        '''
        return self._rpc("checkAirplaneMode")

    def checkRingerSilentMode(self):
        '''
        checkRingerSilentMode()

        Checks the ringer silent mode setting.

        Returns:
          True if ringer silent mode is enabled.
        '''
        return self._rpc("checkRingerSilentMode")

    def checkScreenOn(self):
        '''
        checkScreenOn()

        Checks if the screen is on or off (requires API level 7).

        Returns:
          True if the screen is currently on.
        '''
        return self._rpc("checkScreenOn")

    def getMaxMediaVolume(self):
        '''
        getMaxMediaVolume()

        Returns the maximum media volume.
        '''
        return self._rpc("getMaxMediaVolume")

    def getMaxRingerVolume(self):
        '''
        getMaxRingerVolume()

        Returns the maximum ringer volume.
        '''
        return self._rpc("getMaxRingerVolume")

    def getMediaVolume(self):
        '''
        getMediaVolume()

        Returns the current media volume.
        '''
        return self._rpc("getMediaVolume")

    def getRingerVolume(self):
        '''
        getRingerVolume()

        Returns the current ringer volume.
        '''
        return self._rpc("getRingerVolume")

    def getScreenBrightness(self):
        '''
        getScreenBrightness()

        Returns the screen backlight brightness.

        Returns:
          the current screen brightness between 0 and 255
        '''
        return self._rpc("getScreenBrightness")

    def getScreenTimeout(self):
        '''
        getScreenTimeout()

        Returns the current screen timeout in seconds.

        Returns:
          the current screen timeout in seconds.
        '''
        return self._rpc("getScreenTimeout")

    def getVibrateMode(self,ringer):
        '''
        getVibrateMode(
          Boolean ringer[optional])

        Checks Vibration setting. If ringer=true then query Ringer setting, else query Notification setting

        Returns:
          True if vibrate mode is enabled.
        '''
        return self._rpc("getVibrateMode",ringer)

    def setMediaVolume(self,volume):
        '''
        setMediaVolume(
          Integer volume)

        Sets the media volume.
        '''
        return self._rpc("setMediaVolume",volume)

    def setRingerVolume(self,volume):
        '''
        setRingerVolume(
          Integer volume)

        Sets the ringer volume.
        '''
        return self._rpc("setRingerVolume",volume)

    def setScreenBrightness(self,value):
        '''
        setScreenBrightness(
          Integer value: brightness value between 0 and 255)

        Sets the the screen backlight brightness.

        Returns:
          the original screen brightness.
        '''
        return self._rpc("setScreenBrightness",value)

    def setScreenTimeout(self,value):
        '''
        setScreenTimeout(
          Integer value)

        Sets the screen timeout to this number of seconds.

        Returns:
          The original screen timeout.
        '''
        return self._rpc("setScreenTimeout",value)

    def toggleAirplaneMode(self,enabled):
        '''
        toggleAirplaneMode(
          Boolean enabled[optional])

        Toggles airplane mode on and off.

        Returns:
          True if airplane mode is enabled.
        '''
        return self._rpc("toggleAirplaneMode",enabled)

    def toggleRingerSilentMode(self,enabled):
        '''
        toggleRingerSilentMode(
          Boolean enabled[optional])

        Toggles ringer silent mode on and off.

        Returns:
          True if ringer silent mode is enabled.
        '''
        return self._rpc("toggleRingerSilentMode",enabled)

    def toggleVibrateMode(self,enabled,ringer):
        '''
        toggleVibrateMode(
          Boolean enabled[optional],
          Boolean ringer[optional])

        Toggles vibrate mode on and off. If ringer=true then set Ringer setting, else set Notification setting

        Returns:
          True if vibrate mode is enabled.
        '''
        return self._rpc("toggleVibrateMode",enabled,ringer)


    #******** SignalStrengthFacade Functions : min SDK 7 ********

    def readSignalStrengths(self):
        '''
        readSignalStrengths()

        Returns the current signal strengths.

        Returns:
          A map of "gsm_signal_strength"
        '''
        return self._rpc("readSignalStrengths")

    def startTrackingSignalStrengths(self):
        '''
        startTrackingSignalStrengths()

        Starts tracking signal strengths.

        Generates "signal_strengths" events.
        '''
        return self._rpc("startTrackingSignalStrengths")

    def stopTrackingSignalStrengths(self):
        '''
        stopTrackingSignalStrengths()

        Stops tracking signal strength.
        '''
        return self._rpc("stopTrackingSignalStrengths")


    #******** SmsFacade Functions : min SDK 3 ********

    def smsDeleteMessage(self,id):
        '''
        smsDeleteMessage(
          Integer id)

        Deletes a message.

        Returns:
          True if the message was deleted
        '''
        return self._rpc("smsDeleteMessage",id)

    def smsGetAttributes(self):
        '''
        smsGetAttributes()

        Returns a List of all possible message attributes.
        '''
        return self._rpc("smsGetAttributes")

    def smsGetMessageById(self,id,attributes):
        '''
        smsGetMessageById(
          Integer id: message ID,
          JSONArray attributes[optional])

        Returns message attributes.
        '''
        return self._rpc("smsGetMessageById",id,attributes)

    def smsGetMessageCount(self,unreadOnly,folder):
        '''
        smsGetMessageCount(
          Boolean unreadOnly,
          String folder[optional, default inbox])

        Returns the number of messages.
        '''
        return self._rpc("smsGetMessageCount",unreadOnly,folder)

    def smsGetMessageIds(self,unreadOnly,folder):
        '''
        smsGetMessageIds(
          Boolean unreadOnly,
          String folder[optional, default inbox])

        Returns a List of all message IDs.
        '''
        return self._rpc("smsGetMessageIds",unreadOnly,folder)

    def smsGetMessages(self,unreadOnly,folder,attributes):
        '''
        smsGetMessages(
          Boolean unreadOnly,
          String folder[optional, default inbox],
          JSONArray attributes[optional])

        Returns a List of all messages.

        Returns:
          a List of messages as Maps
        '''
        return self._rpc("smsGetMessages",unreadOnly,folder,attributes)

    def smsMarkMessageRead(self,ids,read):
        '''
        smsMarkMessageRead(
          JSONArray ids: List of message IDs to mark as read.,
          Boolean read)

        Marks messages as read.

        Returns:
          number of messages marked read
        '''
        return self._rpc("smsMarkMessageRead",ids,read)

    def smsSend(self,destinationAddress,text):
        '''
        smsSend(
          String destinationAddress: typically a phone number,
          String text)

        Sends an SMS.
        '''
        return self._rpc("smsSend",destinationAddress,text)


    #******** SpeechRecognitionFacade Functions : min SDK 3 ********

    def recognizeSpeech(self,prompt,language,languageModel):
        '''
        recognizeSpeech(
          String prompt[optional]: text prompt to show to the user when asking them to speak,
          String language[optional]: language override to inform the recognizer that it should expect speech in a language different than the one set in the java.util.Locale.getDefault(),
          String languageModel[optional]: informs the recognizer which speech model to prefer (see android.speech.RecognizeIntent))

        Recognizes user's speech and returns the most likely result.

        Returns:
          An empty string in case the speech cannot be recongnized.
        '''
        return self._rpc("recognizeSpeech",prompt,language,languageModel)


    #******** TextToSpeechFacade Functions : min SDK 4 ********

    def ttsIsSpeaking(self):
        '''
        ttsIsSpeaking()

        Returns True if speech is currently in progress.
        '''
        return self._rpc("ttsIsSpeaking")

    def ttsSpeak(self,message):
        '''
        ttsSpeak(
          String message)

        Speaks the provided message via TTS.
        '''
        return self._rpc("ttsSpeak",message)


    #******** ToneGeneratorFacade Functions : min SDK 3 ********

    def generateDtmfTones(self,phoneNumber,toneDuration):
        '''
        generateDtmfTones(
          String phoneNumber,
          Integer toneDuration[optional, default 100]: duration of each tone in milliseconds)

        Generate DTMF tones for the given phone number.
        '''
        return self._rpc("generateDtmfTones",phoneNumber,toneDuration)


    #******** UiFacade Functions : min SDK 3 ********

    def addContextMenuItem(self,label,event,eventData):
        '''
        addContextMenuItem(
          String label: label for this menu item,
          String event: event that will be generated on menu item click,
          Object eventData[optional])

        Adds a new item to context menu.
        '''
        return self._rpc("addContextMenuItem",label,event,eventData)

    def addOptionsMenuItem(self,label,event,eventData,iconName):
        '''
        addOptionsMenuItem(
          String label: label for this menu item,
          String event: event that will be generated on menu item click,
          Object eventData[optional],
          String iconName[optional]: Android system menu icon, see http://developer.android.com/reference/android/R.drawable.html)

        Adds a new item to options menu.
        '''
        return self._rpc("addOptionsMenuItem",label,event,eventData,iconName)

    def clearContextMenu(self):
        '''
        clearContextMenu()

        Removes all items previously added to context menu.
        '''
        return self._rpc("clearContextMenu")

    def clearOptionsMenu(self):
        '''
        clearOptionsMenu()

        Removes all items previously added to options menu.
        '''
        return self._rpc("clearOptionsMenu")

    def dialogCreateAlert(self,title,message):
        '''
        dialogCreateAlert(
          String title[optional],
          String message[optional])

        Create alert dialog.
        '''
        return self._rpc("dialogCreateAlert",title,message)

    def dialogCreateDatePicker(self,year,month,day):
        '''
        dialogCreateDatePicker(
          Integer year[optional, default 1970],
          Integer month[optional, default 1],
          Integer day[optional, default 1])

        Create date picker dialog.
        '''
        return self._rpc("dialogCreateDatePicker",year,month,day)

    def dialogCreateHorizontalProgress(self,title,message,maximum):
        '''
        dialogCreateHorizontalProgress(
          String title[optional],
          String message[optional],
          Integer maximum progress[optional, default 100])

        Create a horizontal progress dialog.
        '''
        return self._rpc("dialogCreateHorizontalProgress",title,message,maximum)

    def dialogCreateInput(self,title,message,defaultText,inputType):
        '''
        dialogCreateInput(
          String title[optional, default Value]: title of the input box,
          String message[optional, default Please enter value:]: message to display above the input box,
          String defaultText[optional]: text to insert into the input box,
          String inputType[optional]: type of input data, ie number or text)

        Create a text input dialog.
        '''
        return self._rpc("dialogCreateInput",title,message,defaultText,inputType)

    def dialogCreatePassword(self,title,message):
        '''
        dialogCreatePassword(
          String title[optional, default Password]: title of the input box,
          String message[optional, default Please enter password:]: message to display above the input box)

        Create a password input dialog.
        '''
        return self._rpc("dialogCreatePassword",title,message)

    def dialogCreateSeekBar(self,starting,maximum,title,message):
        '''
        dialogCreateSeekBar(
          Integer starting value[optional, default 50],
          Integer maximum value[optional, default 100],
          String title,
          String message)

        Create seek bar dialog.
        '''
        return self._rpc("dialogCreateSeekBar",starting,maximum,title,message)

    def dialogCreateSpinnerProgress(self,title,message,maximum):
        '''
        dialogCreateSpinnerProgress(
          String title[optional],
          String message[optional],
          Integer maximum progress[optional, default 100])

        Create a spinner progress dialog.
        '''
        return self._rpc("dialogCreateSpinnerProgress",title,message,maximum)

    def dialogCreateTimePicker(self,hour,minute,is24hour):
        '''
        dialogCreateTimePicker(
          Integer hour[optional, default 0],
          Integer minute[optional, default 0],
          Boolean is24hour[optional, default false]: Use 24 hour clock)

        Create time picker dialog.
        '''
        return self._rpc("dialogCreateTimePicker",hour,minute,is24hour)

    def dialogDismiss(self):
        '''
        dialogDismiss()

        Dismiss dialog.
        '''
        return self._rpc("dialogDismiss")

    def dialogGetInput(self,title,message,defaultText):
        '''
        dialogGetInput(
          String title[optional, default Value]: title of the input box,
          String message[optional, default Please enter value:]: message to display above the input box,
          String defaultText[optional]: text to insert into the input box)

        Queries the user for a text input.
        '''
        return self._rpc("dialogGetInput",title,message,defaultText)

    def dialogGetPassword(self,title,message):
        '''
        dialogGetPassword(
          String title[optional, default Password]: title of the password box,
          String message[optional, default Please enter password:]: message to display above the input box)

        Queries the user for a password.
        '''
        return self._rpc("dialogGetPassword",title,message)

    def dialogGetResponse(self):
        '''
        dialogGetResponse()

        Returns dialog response.
        '''
        return self._rpc("dialogGetResponse")

    def dialogGetSelectedItems(self):
        '''
        dialogGetSelectedItems()

        This method provides list of items user selected.

        Returns:
          Selected items
        '''
        return self._rpc("dialogGetSelectedItems")

    def dialogSetCurrentProgress(self,current):
        '''
        dialogSetCurrentProgress(
          Integer current)

        Set progress dialog current value.
        '''
        return self._rpc("dialogSetCurrentProgress",current)

    def dialogSetItems(self,items):
        '''
        dialogSetItems(
          JSONArray items)

        Set alert dialog list items.
        '''
        return self._rpc("dialogSetItems",items)

    def dialogSetMaxProgress(self,max):
        '''
        dialogSetMaxProgress(
          Integer max)

        Set progress dialog maximum value.
        '''
        return self._rpc("dialogSetMaxProgress",max)

    def dialogSetMultiChoiceItems(self,items,selected):
        '''
        dialogSetMultiChoiceItems(
          JSONArray items,
          JSONArray selected[optional]: list of selected items)

        Set dialog multiple choice items and selection.
        '''
        return self._rpc("dialogSetMultiChoiceItems",items,selected)

    def dialogSetNegativeButtonText(self,text):
        '''
        dialogSetNegativeButtonText(
          String text)

        Set alert dialog button text.
        '''
        return self._rpc("dialogSetNegativeButtonText",text)

    def dialogSetNeutralButtonText(self,text):
        '''
        dialogSetNeutralButtonText(
          String text)

        Set alert dialog button text.
        '''
        return self._rpc("dialogSetNeutralButtonText",text)

    def dialogSetPositiveButtonText(self,text):
        '''
        dialogSetPositiveButtonText(
          String text)

        Set alert dialog positive button text.
        '''
        return self._rpc("dialogSetPositiveButtonText",text)

    def dialogSetSingleChoiceItems(self,items,selected):
        '''
        dialogSetSingleChoiceItems(
          JSONArray items,
          Integer selected[optional, default 0]: selected item index)

        Set dialog single choice items and selected item.
        '''
        return self._rpc("dialogSetSingleChoiceItems",items,selected)

    def dialogShow(self):
        '''
        dialogShow()

        Show dialog.
        '''
        return self._rpc("dialogShow")

    def fullDismiss(self):
        '''
        fullDismiss()

        Dismiss Full Screen.
        '''
        return self._rpc("fullDismiss")

    def fullKeyOverride(self,keycodes,enable):
        '''
        fullKeyOverride(
          JSONArray keycodes: List of keycodes to override,
          Boolean enable[optional, default true]: Turn overriding or off)

        Override default key actions
        '''
        return self._rpc("fullKeyOverride",keycodes,enable)

    def fullQuery(self):
        '''
        fullQuery()

        Get Fullscreen Properties
        '''
        return self._rpc("fullQuery")

    def fullQueryDetail(self,id):
        '''
        fullQueryDetail(
          String id: id of layout widget)

        Get fullscreen properties for a specific widget
        '''
        return self._rpc("fullQueryDetail",id)

    def fullSetList(self,id,list):
        '''
        fullSetList(
          String id: id of layout widget,
          JSONArray list: List to set)

        Attach a list to a fullscreen widget
        '''
        return self._rpc("fullSetList",id,list)

    def fullSetProperty(self,id,property,value):
        '''
        fullSetProperty(
          String id: id of layout widget,
          String property: name of property to set,
          String value: value to set property to)

        Set fullscreen widget property
        '''
        return self._rpc("fullSetProperty",id,property,value)

    def fullSetTitle(self,title):
        '''
        fullSetTitle(
          String title: Activity Title)

        Set the Full Screen Activity Title
        '''
        return self._rpc("fullSetTitle",title)

    def fullShow(self,layout,title):
        '''
        fullShow(
          String layout: String containing View layout,
          String title[optional]: Activity Title)

        Show Full Screen.
        '''
        return self._rpc("fullShow",layout,title)

    def webViewShow(self,url,wait):
        '''
        webViewShow(
          String url,
          Boolean wait[optional]: block until the user exits the WebView)

        Display a WebView with the given URL.
        '''
        return self._rpc("webViewShow",url,wait)


    #******** WakeLockFacade Functions : min SDK 3 ********

    def wakeLockAcquireBright(self):
        '''
        wakeLockAcquireBright()

        Acquires a bright wake lock (CPU on, screen bright).
        '''
        return self._rpc("wakeLockAcquireBright")

    def wakeLockAcquireDim(self):
        '''
        wakeLockAcquireDim()

        Acquires a dim wake lock (CPU on, screen dim).
        '''
        return self._rpc("wakeLockAcquireDim")

    def wakeLockAcquireFull(self):
        '''
        wakeLockAcquireFull()

        Acquires a full wake lock (CPU on, screen bright, keyboard bright).
        '''
        return self._rpc("wakeLockAcquireFull")

    def wakeLockAcquirePartial(self):
        '''
        wakeLockAcquirePartial()

        Acquires a partial wake lock (CPU on).
        '''
        return self._rpc("wakeLockAcquirePartial")

    def wakeLockRelease(self):
        '''
        wakeLockRelease()

        Releases the wake lock.
        '''
        return self._rpc("wakeLockRelease")


    #******** WebCamFacade Functions : min SDK 8 ********

    def cameraStartPreview(self,resolutionLevel,jpegQuality,filepath):
        '''
        cameraStartPreview(
          Integer resolutionLevel[optional, default 0]: increasing this number provides higher resolution,
          Integer jpegQuality[optional, default 20]: a number from 0-100,
          String filepath[optional]: Path to store jpeg files.)

        Start Preview Mode. Throws 'preview' events.

        Returns:
          True if successful
        '''
        return self._rpc("cameraStartPreview",resolutionLevel,jpegQuality,filepath)

    def cameraStopPreview(self):
        '''
        cameraStopPreview()

        Stop the preview mode.
        '''
        return self._rpc("cameraStopPreview")

    def webcamAdjustQuality(self,resolutionLevel,jpegQuality):
        '''
        webcamAdjustQuality(
          Integer resolutionLevel[optional, default 0]: increasing this number provides higher resolution,
          Integer jpegQuality[optional, default 20]: a number from 0-100)

        Adjusts the quality of the webcam stream while it is running.
        '''
        return self._rpc("webcamAdjustQuality",resolutionLevel,jpegQuality)

    def webcamStart(self,resolutionLevel,jpegQuality,port):
        '''
        webcamStart(
          Integer resolutionLevel[optional, default 0]: increasing this number provides higher resolution,
          Integer jpegQuality[optional, default 20]: a number from 0-100,
          Integer port[optional, default 0]: If port is specified, the webcam service will bind to port, otherwise it will pick any available port.)

        Starts an MJPEG stream and returns a Tuple of address and port for the stream.
        '''
        return self._rpc("webcamStart",resolutionLevel,jpegQuality,port)

    def webcamStop(self):
        '''
        webcamStop()

        Stops the webcam stream.
        '''
        return self._rpc("webcamStop")


    #******** WifiFacade Functions : min SDK 3 ********

    def checkWifiState(self):
        '''
        checkWifiState()

        Checks Wifi state.

        Returns:
          True if Wifi is enabled.
        '''
        return self._rpc("checkWifiState")

    def toggleWifiState(self,enabled):
        '''
        toggleWifiState(
          Boolean enabled[optional])

        Toggle Wifi on and off.

        Returns:
          True if Wifi is enabled.
        '''
        return self._rpc("toggleWifiState",enabled)

    def wifiDisconnect(self):
        '''
        wifiDisconnect()

        Disconnects from the currently active access point.

        Returns:
          True if the operation succeeded.
        '''
        return self._rpc("wifiDisconnect")

    def wifiGetConnectionInfo(self):
        '''
        wifiGetConnectionInfo()

        Returns information about the currently active access point.
        '''
        return self._rpc("wifiGetConnectionInfo")

    def wifiGetScanResults(self):
        '''
        wifiGetScanResults()

        Returns the list of access points found during the most recent Wifi scan.
        '''
        return self._rpc("wifiGetScanResults")

    def wifiLockAcquireFull(self):
        '''
        wifiLockAcquireFull()

        Acquires a full Wifi lock.
        '''
        return self._rpc("wifiLockAcquireFull")

    def wifiLockAcquireScanOnly(self):
        '''
        wifiLockAcquireScanOnly()

        Acquires a scan only Wifi lock.
        '''
        return self._rpc("wifiLockAcquireScanOnly")

    def wifiLockRelease(self):
        '''
        wifiLockRelease()

        Releases a previously acquired Wifi lock.
        '''
        return self._rpc("wifiLockRelease")

    def wifiReassociate(self):
        '''
        wifiReassociate()

        Reassociates with the currently active access point.

        Returns:
          True if the operation succeeded.
        '''
        return self._rpc("wifiReassociate")

    def wifiReconnect(self):
        '''
        wifiReconnect()

        Reconnects to the currently active access point.

        Returns:
          True if the operation succeeded.
        '''
        return self._rpc("wifiReconnect")

    def wifiStartScan(self):
        '''
        wifiStartScan()

        Starts a scan for Wifi access points.

        Returns:
          True if the scan was initiated successfully.
        '''
        return self._rpc("wifiStartScan")

