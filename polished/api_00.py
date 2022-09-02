#ua = "http://github.com/tychobra/polished"


def api_res(resp):

    #if httr::http_type(resp) != "application/json":
    #    stop("API did not return json", call. = FALSE)
    

    parsed = resp.json()

    #if (httr::http_error(resp)) {
    #  cat("Polished API request failed\n")
    #  cat(paste0("Status Code: ", httr::status_code(resp)), "\n")
    #  stop(parsed$error, call. = FALSE)
    #}


    return {
        "content": parsed,
        "response": resp
    }
    