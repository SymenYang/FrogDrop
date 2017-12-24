## source needed
### send requests
1. URI
2. self.IP
3. self.port
4. SIZE
5. User Name
### send response
1. URI
2. UserName
### receive requests
1. URI
2. self.IP
3. self.port
4. start Pos
5. need length(Size)
### receive response 
1. URI
2. self.IP
3. self.port
4. length(Size)
5. file
---
## final protocol (JSON String)
1. Method : PUT/REC/GET/TRS (String)
2. Sender : IP
3. SenderPort : Port
4. Receiver : IP
5. ReceiverPort : Port
6. URI : String
7. UserName : String
8. Size : Int
9. StartPos : Int
10. File : Binary
---
## Sample

### first put request
```
{ 
    Method : PUT,
    Sender : aaa.aaa.aaa.aaa,
    SenderPort : xxxxx(use 36500),
    Receiver : bbb.bbb.bbb.bbb,
    ReceiverPort : xxxxx(use 36500),
    URI : xxx/xxx/xxx.xxx,
    UserName : cccc,
    Size : xxxxx
}
```

### put response
```
{ 
    Method : REC,
    Sender : bbb.bbb.bbb.bbb,
    SenderPort : xxxxx(use 36500),
    Receiver : aaa.aaa.aaa.aaa,
    ReceiverPort : xxxxx(use 36500),
    URI : xxx/xxx/xxx.xxx,
    UserName : dddd
}
```

### Get request
```
{
    Method : GET,
    Sender : bbb.bbb.bbb.bbb,
    SenderPort : xxxxx(use 36501),
    Receiver : aaa.aaa.aaa.aaa,
    ReceiverPort : xxxxx(use 36501),
    URI : xxx/xxx/xxx.xxx,
    StartPos: xxxx,
    Size : xxxx
}
```

### Get response
```
{
    Method : TRS,
    Sender : aaa.aaa.aaa.aaa,
    SenderPort : xxxxx(use 36501),
    Receiver : bbb.bbb.bbb.bbb,
    ReceiverPort : xxxxx(use 36501),
    URI : xxx/xxx/xxx.xxx,
    Size : xxxx,
    File : 01010101...
}
```