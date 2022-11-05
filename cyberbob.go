package main
import (
    "fmt" 
    "net/http"
    "encoding/json"
    "time"
)


type Foo struct{
    Bar string
}

var myClient = &http.Client{Timeout: 10 * time.Second}

func getJson(url string, target interface{}) error {
    r, err := myClient.Get(url)
    if err != nil {
        return err
    }
    defer r.Body.Close()

    return json.NewDecoder(r.Body).Decode(target)
}

func main(){
    foo1:= new(Foo)
    getJson("http://ip-api.com/json",foo1);
    fmt.Println(foo1)
    fmt.Println("======")
}
