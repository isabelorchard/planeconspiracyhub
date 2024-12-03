SwScroll.AJAX = {};
SwScroll.AJAX.createRequest = function () {
    if (typeof XMLHttpRequest != "undefined") {
        return (new XMLHttpRequest())
    } else {
        var a = ["MSXML2.XMLHttp.5.0", "MSXML2.XMLHttp.4.0", "MSXML2.XMLHttp.3.0", "MSXML2.XMLHttp", "Microsoft.XMHttp"];
        var b = null;
        for (var i = 0; i < a.length; i++) {
            try {
                b = new ActiveXObject(a[i]);
                return b
            } catch (e) {}
        }
    }
};
SWSCROLL.loadDynamicContent = function (a, b) {
    var c = this;
    var d = SwScroll.AJAX.createRequest();
    d.open("get", a, true);
    d.setRequestHeader("Cache-Control", "no-cache");
    d.setRequestHeader("If-Modified-Since", "Sat, 1 Jan 2000 00:00:00 GMT");
    d.onreadystatechange = function () {
        if (d.readyState == 4) {
            if (d.status == 200 || d.status == 304) {
                if (d.getResponseHeader("Content-Type").indexOf("text/xml") != -1) {} else {
                    c.setContent(d.responseText);
                    c.ldng.style.display = "none";
                    c.reload();
                    c.start();
                    if (b && b > 0) c.tmDyn = setTimeout(function () {
                        c.loadDynamicContent(a, b)
                    }, b)
                }
            }
        }
    };
    this.ldng.style.display = "";
    d.send(null)
};
SwScroll.$addParam = function (a, b) {
    var s = (a.indexOf("?") != -1 ? "&" : "?");
    return a + s + b
};
SwScroll.AJAX = {};
SwScroll.AJAX.createRequest = function () {
    if (typeof XMLHttpRequest != "undefined") {
        return (new XMLHttpRequest())
    } else {
        var a = ["MSXML2.XMLHttp.5.0", "MSXML2.XMLHttp.4.0", "MSXML2.XMLHttp.3.0", "MSXML2.XMLHttp", "Microsoft.XMHttp"];
        var b = null;
        for (var i = 0; i < a.length; i++) {
            try {
                b = new ActiveXObject(a[i]);
                return b
            } catch (e) {}
        }
    }
};
SWSCROLL.loadDynamicContent = function (a, b) {
    var c = this;
    var d = SwScroll.AJAX.createRequest();
    d.open("get", a, true);
    d.setRequestHeader("Cache-Control", "no-cache");
    d.setRequestHeader("If-Modified-Since", "Sat, 1 Jan 2000 00:00:00 GMT");
    d.onreadystatechange = function () {
        if (d.readyState == 4) {
            if (d.status == 200 || d.status == 304) {
                if (d.getResponseHeader("Content-Type").indexOf("text/xml") != -1) {} else {
                    c.setContent(d.responseText);
                    c.ldng.style.display = "none";
                    c.reload();
                    c.start();
                    if (b && b > 0) c.tmDyn = setTimeout(function () {
                        c.loadDynamicContent(a, b)
                    }, b)
                }
            }
        }
    };
    this.ldng.style.display = "";
    d.send(null)
};
SwScroll.$addParam = function (a, b) {
    var s = (a.indexOf("?") != -1 ? "&" : "?");
    return a + s + b
};
