#include <iostream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>
#include <fstream>
#include <string>
using json = nlohmann::json;

using namespace std;
namespace
{
    std::size_t callback(
            const char* in,
            std::size_t size,
            std::size_t num,
            std::string* out)
    {
        const std::size_t totalBytes(size * num);
        out->append(in, totalBytes);
        return totalBytes;
    }
}

int main(int argc, char *argv[]){
    json output;
    if(argc>1){

        string word= argv[1];
        output["word"]=word;
        std::replace(word.begin(),word.end(),' ','+');
        string url = "https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch="+word;
        CURL* curl = curl_easy_init();
	    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
	    curl_easy_setopt(curl, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);
	    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10);
	    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
	    long httpCode(0);
	    std::unique_ptr<std::string> httpData(new std::string());
	    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callback);
	    curl_easy_setopt(curl, CURLOPT_WRITEDATA, httpData.get());
	    curl_easy_perform(curl);
	    curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &httpCode);
	    curl_easy_cleanup(curl);

        json wikipediasearch = json::parse(*httpData.get());
        if(wikipediasearch["query"]["search"].size()>0){

            int pageid = wikipediasearch["query"]["search"][0]["pageid"];


    

            string str1 = to_string(pageid);
            cout<<str1;

            string newurl = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&pageids="+str1;
            CURL* curl2 = curl_easy_init();
            curl_easy_setopt(curl2, CURLOPT_URL, newurl.c_str());
            curl_easy_setopt(curl2, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);
            curl_easy_setopt(curl2, CURLOPT_TIMEOUT, 10);
            curl_easy_setopt(curl2, CURLOPT_FOLLOWLOCATION, 1L);
            long httpCode(0);
            std::unique_ptr<std::string> httpData2(new std::string());
            curl_easy_setopt(curl2, CURLOPT_WRITEFUNCTION, callback);
            curl_easy_setopt(curl2, CURLOPT_WRITEDATA, httpData2.get());
            curl_easy_perform(curl2);
            curl_easy_getinfo(curl2, CURLINFO_RESPONSE_CODE, &httpCode);
            curl_easy_cleanup(curl2);

            cout<<"\n";
            json summaryparser = json::parse(*httpData2.get());
            cout<<"\n";
            string summary = summaryparser["query"]["pages"][str1]["extract"];
            cout<< summary;
            output["pageid"] = pageid;
            
            output["sum"] = summary;
            std::ofstream o("out.json");
		    o << std::setw(4) << output << std::endl;


        }else{
            cout<<"No result\n";
        }
        
    }
}