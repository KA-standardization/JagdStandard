'''
Requests 首先在 HTTP 头部检测是否存在指定的编码方式，如果不存在，则会使用 charade 来尝试猜测编码方式

只有当 HTTP 头部不存在明确指定的字符集，并且 Content-Type 头部字段包含 text 值之时， Requests 才不去猜测编码方式
在这种情况下， RFC 2616 指定默认字符集必须是 ISO-8859-1 。Requests 遵从这一规范。如果你需要一种不同的编码方式，你可以手动设置 Response.encoding 属性，
或使用原始的 Response.content


'''