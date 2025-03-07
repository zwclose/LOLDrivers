+++

description = ""
title = "95d244a5-fa5b-4bcb-a2fd-39ed6c7ea7a4"
weight = 10

+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}


# rtkio64.sys ![:inline](/images/twitter_verified.png) 


### Description

rtkio64.sys is a vulnerable driver and more information will be added as found.
- **UUID**: 95d244a5-fa5b-4bcb-a2fd-39ed6c7ea7a4
- **Created**: 2023-01-09
- **Author**: Michael Haag
- **Acknowledgement**:  | [](https://twitter.com/)

{{< button "https://github.com/magicsword-io/LOLDrivers/raw/main/drivers/70dcd07d38017b43f710061f37cb4a91.bin" "Download" >}}
{{< tip "warning" >}}
This download link contains the vulnerable driver!

{{< /tip >}}

### Commands

```
sc.exe create rtkio64.sys binPath=C:\windows\temp\rtkio64.sys type=kernel &amp;&amp; sc.exe start rtkio64.sys
```

| Use Case | Privileges | Operating System | 
|:---- | ---- | ---- |
| Elevate privileges | kernel | Windows 10 |

### Resources
<br>
<li><a href=" https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md"> https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md</a></li>
<li><a href="https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md">https://github.com/eclypsium/Screwed-Drivers/blob/master/DRIVERS.md</a></li>
<br>

### Known Vulnerable Samples

| Property           | Value |
|:-------------------|:------|
| Filename           | rtkio64.sys |
| MD5                | [70dcd07d38017b43f710061f37cb4a91](https://www.virustotal.com/gui/file/70dcd07d38017b43f710061f37cb4a91) |
| SHA1               | [99201c9555e5faf6e8d82da793b148311f8aa4b8](https://www.virustotal.com/gui/file/99201c9555e5faf6e8d82da793b148311f8aa4b8) |
| SHA256             | [7133a461aeb03b4d69d43f3d26cd1a9e3ee01694e97a0645a3d8aa1a44c39129](https://www.virustotal.com/gui/file/7133a461aeb03b4d69d43f3d26cd1a9e3ee01694e97a0645a3d8aa1a44c39129) |
| Authentihash MD5   | [dbe68427fd1f2194715b4d146dedeae7](https://www.virustotal.com/gui/search/authentihash%253Adbe68427fd1f2194715b4d146dedeae7) |
| Authentihash SHA1  | [118ebc5c7ac859d17c14ceeaa8ab973d694fdd7b](https://www.virustotal.com/gui/search/authentihash%253A118ebc5c7ac859d17c14ceeaa8ab973d694fdd7b) |
| Authentihash SHA256| [e46bb410c3bb95a1f3d61ced157c679bfac7dc997534e46b83b234a6fc5cbb14](https://www.virustotal.com/gui/search/authentihash%253Ae46bb410c3bb95a1f3d61ced157c679bfac7dc997534e46b83b234a6fc5cbb14) |
| Company           | Realtek                                             |
| Description       | Realtek IO Driver |
| Product           | Realtek IO Driver                       |
| OriginalFilename  | rtkio64.sys  |


#### Imports
{{< details "Expand" >}}
* ntoskrnl.exe
* HAL.dll

{{< /details >}}
#### ImportedFunctions
{{< details "Expand" >}}
* MmMapIoSpace
* MmUnmapLockedPages
* ExUnregisterCallback
* ExAllocatePoolWithTag
* IoWMIRegistrationControl
* KeQueryActiveProcessors
* IoDeleteSymbolicLink
* ExFreePoolWithTag
* IoWMIWriteEvent
* IoRegisterShutdownNotification
* RtlInitUnicodeString
* IoDeleteDevice
* MmGetSystemRoutineAddress
* MmBuildMdlForNonPagedPool
* IoFreeMdl
* MmUnmapIoSpace
* ZwQueryValueKey
* IoUnregisterShutdownNotification
* ZwClose
* IofCompleteRequest
* ExRegisterCallback
* RtlCompareMemory
* IoCreateSymbolicLink
* KeSetSystemAffinityThread
* ObfDereferenceObject
* IoCreateDevice
* ExCreateCallback
* IoAllocateMdl
* ZwOpenKey
* KeBugCheckEx
* MmMapLockedPagesSpecifyCache
* _vsnprintf
* __C_specific_handler
* KeStallExecutionProcessor

{{< /details >}}
#### ExportedFunctions
{{< details "Expand" >}}

{{< /details >}}

#### Signature
{{< details "Expand" >}}
```
{
  "Certificates": [
    {
      "Signature": "208cc159ed6f9c6b2dc14a3e751d454c41501cbd80ead9b0928b062a133f53169e56396a8a63b6782479f57db8b947a10a96c2f6cbbda2669f06e1acd279090efd3cdcac020c70af3f1bec787ed4eb4b056026d973619121edb06863e09712ab6fa012edd99fd2da273cb3e456f9d1d4810f71bd427ca689dccdd5bd95a2abf193117de8ac3129a85d6670419dfc75c9d5b31a392ad08505508bac91cac493cb71a59da4946f580cfa6e20c40831b5859d7e81f9d23dca5b18856c0a86ec22091ba574344f7f28bc954aab1db698b05d09a477767eefa78e5d84f61824cbd16da6c3a19cc2107580ff9d32fde6cf433a82f7ce8fe1722a9b62b75fed951a395c2f946d48b7015f332fbbdc2d73348904420a1c8b79f9a3fa17effaa11a10dfe0b2c195eb5c0c05973b353e18884ddb6cbf24898dc8bdd89f7b393a24a0d5dfd1f34a1a97f6a66f7a1fb090a9b3ac013991d361b764f13e573803afce7ad2b590f5aedc3999d5b63c97eda6cb16c77d6b2a4c9094e64c54fd1ecd20ecce689c8758e96160beeb0ec9d5197d9fe978bd0eac2175078fa96ee08c6a2a6b9ce3e765bcbc2d3c6ddc04dc67453632af0481bca8006e614c95c55cd48e8e9f2fc13274bdbd11650307cdefb75e0257da86d41a2834af8849b2cfa5dd82566f68aa14e25954feffeaeeefea9270226081e32523c09fcc0f49b235aa58c33ac3d9169410",
      "SignatureAlgorithmOID": "1.2.840.113549.1.1.5",
      "Subject": "C=US, O=DigiCert Inc, OU=www.digicert.com, CN=DigiCert High Assurance EV Root CA",
      "ValidFrom": "2011-04-15 19:45:33",
      "ValidTo": "2021-04-15 19:55:33"
    },
    {
      "Signature": "9616a10e728762896fad0b74d574eb1775ae3bd1b12dc07441d668ec373ffb2ed5590d43f821b8d440c8e11338272d0cd1bc0ea5c05a428538c0ba1195e800c51e81db998174bdbe25be284a2c367d3578cf801524bd9f18b9098f4ee79f45a0e9af74894b828523f0b2c1c6837bc572da3be7f769e8df8749f26fd05087cc4b09fedac11c037e3690441286f8c52c09f18c7c179138f4844a8d99d8f9e7dec178ead089e12a05469c046a3c85b43d038811f02c6803128bf9bc1b757a2bb72d3ad61f670d3ae856ade0165f9dff89c36592b5295ead0718458c19c2f21781cd1ef0685049ebddd88806cd17e6eab078e2f0a505845ee5d9fca6904260ef8a1a",
      "SignatureAlgorithmOID": "1.2.840.113549.1.1.5",
      "Subject": "??=Private Organization, ??=TW, serialNumber=22671299, ??=No. 2, Innovation Road II, Hsinchu Science Park, postalCode=300, C=TW, ST=Taiwan, L=Hsinchu, O=Realtek Semiconductor Corp., CN=Realtek Semiconductor Corp.",
      "ValidFrom": "2016-06-13 00:00:00",
      "ValidTo": "2019-01-24 12:00:00"
    },
    {
      "Signature": "9d257e1b334db226815c9b86ce23200f8087e588ffffb1d46a2c31ed3a17197117cda91bbc5a1639009de36c84e45a40fbde06018c37fa9bb19d247efe20a457ad5bb79ab06026ea6957215d342f1f71b0839419056b359010a07b97c7f63fe7e21141a6bd62d9f0273d381d286f3a5209f0ec7062d3624bb0e073a692c0d38e31d82fe36d171306eee403b614abf38f43a7719d21dd14ca155d9241daf90f81d199740d26c40e7f1bb5f5a0f1c677062815e9d893e55516f0bb0aab1cdb5c482766c8a38b0a1ce595daaec42e59a061dddaf36da261e98a0b6dec1218bdf755544003922b6bc251c20a48afb0d46ee0f4140a3a1be38f3dcaaf6a8d7bdcd844",
      "SignatureAlgorithmOID": "1.2.840.113549.1.1.5",
      "Subject": "C=US, O=DigiCert, CN=DigiCert Timestamp Responder",
      "ValidFrom": "2014-10-22 00:00:00",
      "ValidTo": "2024-10-22 00:00:00"
    },
    {
      "Signature": "9e5b963a2e1288acab016da49f75e40187a3a532d7bcbaa97ea3d61417f7c2136b7c738f2b6ae50f265968b08e259b6ceffa6c939208c14dcf459e9c46d61e74a19b14a3fa012f4ab101e1724048111368b9369d914bd7c2391210c1c4dcbb6214142a615d4f387c661fc61bffadbe4f7f945b7343000f4d73b751cf0ef677c05bcd348cd96313aa0e6111d6f28e27fcb47bb8b91120918678ea0ed428ff2ad52438e837b2ec96bb9fbc4a1650e15ebf517d23a032c7c1949e7ac9c026a2cc2587a0127e749f2d8db1c8e784beb9d1e9debb6a4e887371e12238cb2487e9737e51b2ff98eb4e7e2fe0ca0efab35ed1ba0542a8489f83f63fc4caa8df68a05061",
      "SignatureAlgorithmOID": "1.2.840.113549.1.1.5",
      "Subject": "C=US, O=DigiCert Inc, OU=www.digicert.com, CN=DigiCert EV Code Signing CA",
      "ValidFrom": "2012-04-18 12:00:00",
      "ValidTo": "2027-04-18 12:00:00"
    },
    {
      "Signature": "46503ec9b72824a7381db65b29af52cf52e93147ab565c7bd50d0b41b3efec751f7438f2b25c61a29c95c350e482b923d1ba3a8672ad3878ac755d1717347247859456d1ebbb368477cc24a5f3041955a9e7e3e7ab62cdfb8b2d90c2c0d2b594bd5e4fb105d20e3d1aa9145ba6863162a8a833e49b39a7c4f5ce1d7876942573e42aabcf9c764bed5fc24b16e44b704c00891efcc579bc4c1257fe5fe11ebc025da8fefb07384f0dc65d91b90f6745cdd683ede7920d8db1698c4ffb59e0230fd2aaae007cee9c420ecf91d727b716ee0fc3bd7c0aa0ee2c08558522b8eb181a4dfc2a21ad49318347957771dcb11b4b4b1c109c7714c19d4f2f5a9508291026",
      "SignatureAlgorithmOID": "1.2.840.113549.1.1.5",
      "Subject": "C=US, O=DigiCert Inc, OU=www.digicert.com, CN=DigiCert Assured ID CA,1",
      "ValidFrom": "2006-11-10 00:00:00",
      "ValidTo": "2021-11-10 00:00:00"
    }
  ],
  "CertificatesInfo": "",
  "Signer": [
    {
      "Issuer": "C=US, O=DigiCert Inc, OU=www.digicert.com, CN=DigiCert EV Code Signing CA",
      "SerialNumber": "0320be3eb866526927f999b97b04346e"
    }
  ],
  "SignerInfo": ""
}
```

{{< /details >}}
-----



[*source*](https://github.com/magicsword-io/LOLDrivers/tree/main/yaml/95d244a5-fa5b-4bcb-a2fd-39ed6c7ea7a4.yaml)

*last_updated:* 2023-05-12








{{< /column >}}
{{< /block >}}
