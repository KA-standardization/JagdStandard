# ElasticSearch

```shell
curl 'localhost:9200/bbs_yjs/_count?pretty'
```

```shell
curl 'http://127.0.0.1:9200/bbs_yjs/_search?pretty' -d '{
  "query": {
    "query_string": {
      "query": "1030314",
      "default_field": "post_id",
      "default_operator": "AND"
    }
  }
}' -H 'content-Type:application/json' 
```

```shell
curl 'http://127.0.0.1:9200/bbs_yjs/_search?pretty' -d '{
  "query": {
    "bool": {
      "filter": {
        "term": {
          "post_id": "1030314"
        }
      }
    }
  }
}' -H 'content-Type:application/json'
```

```shell
curl 'http://127.0.0.1:9200/bbs_yjs/_search?pretty' -d '{
  "aggregations": {
    "organizers": {
      "terms": {
        "field": "p"
      }
    }
  }
}' -H 'content-Type:application/json'
```

```shell
curl 'http://127.0.0.1:9200/bbs_yjs/group/1011?pretty'
```

```shell
curl XPUT 'http://127.0.0.1:9200/bbs_yjs/_mapping/new-events' -d '{
"new-events":{
"properties":{
"name":{
"type":"string",
"index":"not_analyzed"
}
}
}
}'
```

```
curl -u eswriter:ZDM4MTUwZDNi 'http://10.0.4.102:4040/bbs_yjs/_mapping?pretty' -H 'content-Type:application/json'

curl -X PUT -u eswriter:ZDM4MTUwZDNi 'http://10.0.4.102:4040/bbs_yjs/_mapping/' -d '{"properties": {"is_ok": {"type": "keyword"}}}' -H 'content-Type:application/json'
```

