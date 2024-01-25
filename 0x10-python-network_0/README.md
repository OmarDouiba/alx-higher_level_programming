# 0x10. Python - Network #0

---

## Resources

---

- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [How To Use The cURL Command](https://www.youtube.com/watch?v=WxUVU0b95Oc)
- [curl tutorial](https://curl.se/docs/tutorial.html)

## General

---

#### What a URL is

-

#### What HTTP is

- HTTP (Hypertext Transfer Protocol) is a protocol built on top of the TCP/IP stack at the application layer. It operates by following a set of rules and conventions to transfer hypertext, which includes text, links, images, and other multimedia content. This protocol facilitates communication between a web server and a client, typically a web browser.

#### How to read a URL

- To interpret a URL, the process typically begins from the left and progresses towards the right.

```
    https://www.example.com/path/to/resource?q=term#section
```

- **Host** (https): The URL usually begins with the protocol, such as "http://" or "https://". This indicates the communication protocol to be used, with "http" being unencrypted and "https" being encrypted (secured using SSL/TLS).

- **_Host_** ("www.example.com"): Following the protocol is the host, which includes the subdomain (if present), domain name, and top-level domain (TLD). These parts are separated by dots. For example, in "www.example.com", "www" is the subdomain, "example" is the domain name, and "com" is the TLD.

- **_Path_** ("/path/to/resource"): After the host, a forward slash ("/") may indicate the root or a specific path on the server. This part of the URL specifies the location of the resource on the server. For example, in "www.example.com/path/to/resource", "/path/to/resource" is the path.

- **_Query Parameters_** ( "?q=term"): Following the path, if there are query parameters, they are separated by a question mark ("?"). Query parameters provide additional information to the server, often in the form of key-value pairs. For example, in "www.example.com/search?q=term", "?q=term" is the query parameter indicating a search for the term "term".

- **_Fragment Identifier_** ("#section"): If there is a fragment identifier, it is indicated by a hash ("#"). The fragment identifier points to a specific section within the resource. For example, in "www.example.com/page#section", "#section" is the fragment identifier.

#### The scheme for a HTTP URL

-

#### What a domain name is

-

#### What a sub-domain is

-

#### How to define a port number in a URL

-

#### What a query string is

-

#### What an HTTP request is

-

#### What an HTTP response is

-

#### What HTTP headers are

-

#### What the HTTP message body is

-

#### What an HTTP request method is

-

#### What an HTTP response status code is

-

#### What an HTTP Cookie is

-

#### How to make a request with cURL

-

#### What happens when you type google.com in your browser (Application level)

-
