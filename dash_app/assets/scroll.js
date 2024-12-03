var swScroll = new Object();
var _ua = window.navigator.userAgent;
var sw_isIE = (_ua.indexOf("MSIE") >= 0);
var sw_isIE5 = (_ua.indexOf("MSIE 5.0") >= 0);
var sw_isIE4 = (_ua.indexOf("MSIE 4") >= 0);
var sw_isSafari = (_ua.indexOf("Safari") >= 0);
var sw_isOpera = (_ua.indexOf("Opera") >= 0);
if (sw_isOpera) sw_isIE = false;

function SwScrollIco(a) {
    if (!a || a == "") {
        var b = (document.getElementsByTagName ? document.getElementsByTagName("SCRIPT") : document.scripts);
        for (var i = 0; i < b.length; i++) {
            if (b[i].src.toLowerCase().indexOf("scroll.js") >= 0) {
                a = b[i].src.replace(/scroll.js/gi, "img/");
                break
            }
        }
    }
    this.next = a + "next.gif";
    this.nextover = a + "nextover.gif";
    this.prev = a + "prev.gif";
    this.prevover = a + "prevover.gif";
    this.resume = a + "play.gif";
    this.resumeover = a + "playover.gif";
    this.stop = a + "stop.gif";
    this.stopover = a + "stopover.gif";
    this.backgrd = a + "bg.gif";
    this.modeauto = a + "modeauto.gif";
    this.modeman = a + "modeman.gif";
    this.loading = a + "loading.gif";
    return this
};

function SwScroll(s) {
    this.scrlId = s;
    this.intRef = null;
    this.blockObj = null;
    this.helper = null;
    this.ico = new SwScrollIco();
    swScroll[s] = this;
    this.mode = "AUTO";
    this.effect = new EffContinuous();
    this.showToolbar = false;
    this.toolbar = ["MODE", "PLAY", "PREV", "NEXT"];
    this.content = [];
    this.width = 150;
    this.height = 80;
    this.speed = 3500;
    this.stylePref = "";
    this.stopOnMouseOver = false;
    this.loadText = "Loading...";
    this.prev = function () {
        this.effect.prev()
    };
    this.next = function () {
        this.effect.next()
    };
    this.onMouseOver = function () {};
    this.onMouseOut = function () {};
    return this
};
var SWSCROLL = SwScroll.prototype;
SWSCROLL.setContent = function (c) {
    var a = c.match(/<body[^>]/gi);
    if (a) {
        c = c.substr(c.indexOf(a[0]));
        c = c.substr(c.indexOf(">") + 1);
        a = c.match(/<\/body>/gi);
        if (a) {
            c = c.substr(0, c.indexOf(a[0]))
        }
    }
    var s = "<span class=\"swscrollerbreak\"></span>";
    c = c.replace(/<span class=(["']*)swscrollerbreak(["']*)><\/span>/gi, s);
    this.content = c.split(s);
    this.reload()
};
SWSCROLL.setContentById = function (a) {
    var b = SwScroll.GE(a);
    b.style.overflow = "hidden";
    this.setContent(b.innerHTML)
};
SwScroll.$posAttr = function () {
    var a = "absolute",
        dsp = "none";
    if (sw_isIE4) {
        a = "absolute";
        dsp = "block"
    }
    return [a, dsp]
};
SwScroll.$genContent = function (c) {
    var a = "",
        atr = SwScroll.$posAttr();
    for (var i = 0; i < c.content.length; i++) {
        a += ("<table id='" + c.scrlId + "line" + i + "' style='display:" + atr[1] + ";position:absolute;top:0px' class='" + c.stylePref + "scrlcontentfrm'><tr><td class='" + c.stylePref + "scrlcontent'>" + c.content[i] + "</td></tr></table>")
    }
    return a
};
SWSCROLL.render = function (a) {
    var b = SwScroll.$posAttr(),
        sId = this.scrlId,
        sObj = "swScroll." + sId;
    var c = "<table id='" + sId + "auto' cellpadding='0' cellspacing='0' " + (this.mode == "MANUAL" ? "style='display:none'" : "") + "><tr>";
    c += "<td onmouseover=\"SwScroll.tbMOVR('" + sId + "play')\" onmouseout=\"SwScroll.tbMOUT('" + sId + "play')\" onclick='" + sObj + ".resume();'><img id='" + sId + "play' src='" + this.ico.resume + "' alt='Run' ><img id='" + sId + "playover' src='" + this.ico.resumeover + "' style='display:none' alt='Play'></td>";
    c += "<td onmouseover=\"SwScroll.tbMOVR('" + sId + "pause')\" onmouseout=\"SwScroll.tbMOUT('" + sId + "pause')\" onclick='" + sObj + ".stop();'><img id='" + sId + "pause' src='" + this.ico.stop + "' alt='Stop'><img id='" + sId + "pauseover' src='" + this.ico.stopover + "' style='display:none' alt='Stop'></td>";
    c += "</tr></table>";
    var d = "<table id='" + sId + "manual' border='0' cellpadding='0' cellspacing='0' " + (this.mode == "AUTO" ? "style='display:none'" : "") + "><tr>";
    d += "<td onmouseover=\"SwScroll.tbMOVR('" + sId + "prev')\" onmouseout=\"SwScroll.tbMOUT('" + sId + "prev')\" onclick='" + sObj + ".prev();'><img id='" + sId + "prev' src='" + this.ico.prev + "' alt='Previous'><img id='" + sId + "prevover' src='" + this.ico.prevover + "' style='display:none' alt='Previous'></td>";
    d += "<td onmouseover=\"SwScroll.tbMOVR('" + sId + "next')\" onmouseout=\"SwScroll.tbMOUT('" + sId + "next')\" onclick='" + sObj + ".next();'><img id='" + sId + "next' src='" + this.ico.next + "' alt='Next'><img id='" + sId + "nextover' src='" + this.ico.nextover + "' style='display:none' alt='Next'></td>";
    d += "</tr></table>";
    var e = "<table cellpadding='0' cellspacing='0'><tr><td onclick='" + sObj + ".toggleMode();'><img id='" + sId + "mode' src='" + this.ico.modeauto + "' " + (this.mode == "MANUAL" ? "style='display:none'" : "") + " alt='Toggle scroll mode: auto/manual'><img id='" + sId + "modeover' src='" + this.ico.modeman + "' " + (this.mode == "AUTO" ? "style='display:none'" : "") + " alt='Toggle scroll mode: auto/manual'></td></tr></table>";
    var f = "<table id=\"" + sId + "$loading\" style='display:none;position:absolute;top:z-index:1000'><tr><td><img src='" + this.ico.loading + "'></td><td style='color:#333333'>" + this.loadText + "</td></tr></table>";
    var g = SwScroll.$genContent(this);
    g = "<div id=\"" + sId + "$content\" style='height:100%'>" + g + "</div>";
    g += ("<div id='" + sId + "Helper' style='display:" + b[1] + ";position:absolute;top:0px;width:100%;height:100%' class='" + this.stylePref + "scrlefflayerH'><table width='100%' cellpadding='0' cellspacing='0'><tr><td></td></tr></table></div>");
    g = ("<div id=\"" + sId + "\" style='position:absolute;overflow:hidden;width:" + this.width + "px;height:" + this.height + "px;' onmouseover=\"SwScroll.mOver('" + sId + "')\" onmouseout=\"SwScroll.mOut('" + sId + "')\">" + g + "</div>");
    g = "<table cellpadding='0' cellspacing='0'><tr><td valign='top' style='width:" + this.width + "px;height:" + this.height + "px'>" + g;
    g += "</td></tr></table>";
    g = "<table cellpadding='0' cellspacing='0' class='" + this.stylePref + "swscroller'><tr><td class='" + this.stylePref + "scrlclient'>" + f + g + "</td></tr>";
    if (this.showToolbar && this.toolbar.length > 0) g += "<tr><td class='" + this.stylePref + "scrltoolbar' background='" + this.ico.backgrd + "' align='center'><table width='100%' height='100%' cellpadding='0' cellspacing='0'><tr><td width='20px'>&nbsp;</td><td align='center'>" + c + d + "</td><td width='20px'>" + e + "</td></tr></table></td></tr>";
    g += "</table>";
    if (a) {
        var h = SwScroll.GE(a);
        h.innerHTML = g;
        h.style.display = "block"
    } else {
        document.write(g);
        g = ""
    }
    this.helper = SwScroll.GE(sId + "Helper");
    this.scrl = SwScroll.GE(sId);
    this.cntWin = SwScroll.GE(sId + "$content");
    this.ldng = SwScroll.GE(sId + "$loading");
    if (sw_isIE) {
        window.attachEvent("onload", function () {
            swScroll[sId].start()
        })
    } else {
        window.addEventListener("load", function () {
            swScroll[sId].start()
        }, false)
    }
    return g
};
SWSCROLL.reload = function () {
    if (!this.cntWin) return;
    this.stop();
    this.cntWin.innerHTML = SwScroll.$genContent(this)
};
SWSCROLL.start = function () {
    var a = null;
    this.blockObj = [];
    for (var i = 0; i < this.content.length; i++) {
        a = SwScroll.GE(this.scrlId + "line" + i);
        this.blockObj[this.blockObj.length] = a;
        with(a.style) {
            zIndex = this.content.length - i;
            display = ""
        }
    }
    if (this.blockObj.length == 0) return;
    this.effect.init(this);
    this.stop();
    if (this.effect.name == "EffContinuous") {
        this.intRef = setTimeout("eval(swScroll." + this.scrlId + ".effect.run())", this.speed)
    } else {
        if (this.mode == "AUTO") {
            this.intRef = setInterval("eval(swScroll." + this.scrlId + ".effect.run())", this.speed)
        }
    }
};
SWSCROLL.stop = function () {
    if (!this.effect) return;
    if (this.effect.name == "EffContinuous") {
        this.effect.stop();
        if (this.intRef) {
            clearTimeout(this.intRef);
            this.intRef = null
        }
    } else {
        if (this.intRef) {
            clearInterval(this.intRef);
            this.intRef = null
        }
    }
};
SWSCROLL.resume = function () {
    if (!this.effect) return;
    if (this.effect.name == "EffContinuous") {
        this.effect.run()
    } else {
        if (this.intRef == null) {
            this.intRef = setInterval("eval(swScroll." + this.scrlId + ".effect.run())", this.speed)
        }
    }
};
SWSCROLL.toggleMode = function () {
    var m = SwScroll.GE(this.scrlId + "mode");
    var a = SwScroll.GE(this.scrlId + "modeover");
    var b = SwScroll.GE(this.scrlId + "manual");
    var c = SwScroll.GE(this.scrlId + "auto");
    if (this.mode == "AUTO") {
        if (this.effect.name == "EffContinuous") {
            alert("Manual mode not available in this effect");
            return
        }
        this.mode = "MANUAL";
        this.stop();
        m.style.display = "none";
        a.style.display = "";
        b.style.display = "";
        c.style.display = "none"
    } else if (this.mode == "MANUAL") {
        this.mode = "AUTO";
        this.effect.cfg["topicsequence"] = "next";
        this.resume();
        m.style.display = "";
        a.style.display = "none";
        b.style.display = "none";
        c.style.display = ""
    }
};
SWSCROLL.setEffect = function (a) {
    if (!a) return;
    if (a.name == "EffContinuous") {
        if (SwScroll.GE(this.scrlId + "mode")) {
            if (this.mode == "MANUAL") this.toggleMode()
        } else {
            this.mode = "AUTO"
        }
    } else if (a.name == "EffIETrans") {
        if (!sw_isIE || sw_isIE5) return
    } else if (a.name == "EffFade") {
        if (sw_isOpera || sw_isIE5) return
    }
    this.stop();
    this.effect = a
};
SwScroll.GE = function (a) {
    if (document.all) {
        return document.all(a)
    } else if (document.getElementById) {
        return document.getElementById(a)
    }
};
SwScroll.exitView = function (a, b, c) {
    switch (a) {
    case "up":
        ;
    case "left":
        return (b <= c);
    case "down":
        ;
    case "right":
        return (b >= c)
    }
};
SwScroll.prevTopic = function () {
    this.cfg.topicsequence = "prev";
    this.run()
};
SwScroll.nextTopic = function () {
    this.cfg.topicsequence = "next";
    this.run()
};
SwScroll.setTopic = function () {
    this.crTpc = SwScroll.getTopic(this)
};
SwScroll.getTopic = function (f) {
    var a = f.scr.blockObj.length,
        tp = f.crTpc;
    if (f.cfg.topicsequence == "next") {
        tp = (tp == a - 1 ? 0 : tp + 1)
    } else {
        tp = (tp == 0 ? a - 1 : tp - 1)
    }
    return tp
};
SwScroll.tbMOVR = function (b) {
    SwScroll.GE(b).style.display = "none";
    SwScroll.GE(b + "over").style.display = ""
};
SwScroll.tbMOUT = function (b) {
    SwScroll.GE(b).style.display = "";
    SwScroll.GE(b + "over").style.display = "none"
};
SwScroll.mOver = function (a) {
    var b = swScroll[a];
    if (b.mode == "MANUAL") return;
    if (b.stopOnMouseOver) b.stop();
    b.onMouseOver()
};
SwScroll.mOut = function (a) {
    var b = swScroll[a];
    if (b.mode == "MANUAL") return;
    if (b.stopOnMouseOver) b.resume();
    b.onMouseOut()
};

function EffContinuous(f) {
    var g = this;
    this.scr = null;
    this.rtprop = {};
    this.cfg = {
        direction: "up",
        speed: 40,
        step: 1,
        delay: 0
    };
    if (f && f != "") {
        var h = f.replace(/\s+/gi, "").toLowerCase().split(",");
        var j = "";
        for (var i = 0; i < h.length; i++) {
            j = h[i].split("=");
            this.cfg[j[0]] = j[1]
        }
    }
    this.crTpc = 0;
    this.lsTpc = null;
    this.name = "EffContinuous";
    this.init = function (a) {
        this.scr = a;
        this.crTpc = 0;
        var b = null;
        var c = 0;
        for (var i = 0; i < this.scr.blockObj.length; i++) {
            b = this.scr.blockObj[i];
            b.style.height = "";
            with(b.style) {
                switch (this.cfg["direction"]) {
                case "up":
                    left = 0;
                    top = c + "px";
                    c += b.offsetHeight;
                    break;
                case "down":
                    left = 0;
                    c += b.offsetHeight;
                    top = (this.scr.height - c) + "px";
                    break;
                case "left":
                    top = 0;
                    left = c + "px";
                    c += b.offsetWidth;
                    break;
                case "right":
                    top = 0;
                    c += b.offsetWidth;
                    left = (this.scr.width - c) + "px";
                    break
                }
            }
        }
        this.lsTpc = b
    };
    this.run = function () {
        if (!this.scr) return;
        var a = 1,
            dir, odim, dim, sdir = this.cfg["direction"];
        switch (sdir) {
        case "up":
        case "left":
            this.runScroll = runUpLeft;
            a = -this.cfg["step"];
            break;
        case "down":
        case "right":
            this.runScroll = runDownRight;
            a = +this.cfg["step"];
            break
        }
        switch (sdir) {
        case "up":
        case "down":
            dir = "top";
            odim = "offsetHeight";
            dim = "height";
            break;
        case "left":
        case "right":
            dir = "left";
            odim = "offsetWidth";
            dim = "width";
            break
        }
        this.stop();
        this.rtprop["tmId"] = window.setInterval(function () {
            g.runScroll(a, dir, odim, dim)
        }, +g.cfg["speed"])
    };
    this.runScroll = function () {};

    function runUpLeft(a, b, c, d) {
        var l, pos, bl = this.scr.blockObj;
        for (var i = 0; i < bl.length; i++) {
            l = bl[i];
            pos = parseInt(l.style[b]) + a;
            l.style[b] = pos + "px";
            if (pos > this.scr[d]) {
                pos = parseInt(bl[i - 1].style[b]) + bl[i - 1][c];
                l.style[b] = pos + "px";
                break
            }
        }
        l = bl[0];
        pos = parseInt(l.style[b]);
        var e = -l[c];
        if (SwScroll.exitView(this.cfg["direction"], pos, e)) {
            var t = parseInt(this.lsTpc.style[b]) + this.lsTpc[c];
            l.style[b] = (t > this.scr[d] ? t : this.scr[d]) + "px";
            this.lsTpc = l;
            for (var i = 0; i < bl.length - 1; i++) {
                bl[i] = bl[i + 1]
            }
            bl[i] = l;
            if (+this.cfg["delay"] > 0) {
                this.stop();
                setTimeout(function () {
                    g.run()
                }, +this.cfg["delay"])
            }
        }
    };

    function runDownRight(a, b, c, d) {
        var l, pos, bl = this.scr.blockObj;
        for (var i = 0; i < bl.length; i++) {
            l = bl[i];
            pos = parseInt(l.style[b]) + a;
            l.style[b] = pos + "px";
            if (pos + l[c] < 0) {
                pos = parseInt(bl[i - 1].style[b]) - l[c];
                l.style[b] = pos + "px";
                break
            }
        }
        l = bl[0];
        pos = parseInt(l.style[b]);
        var e = this.scr[d];
        if (SwScroll.exitView(this.cfg["direction"], pos, e)) {
            var t = parseInt(this.lsTpc.style[b]);
            l.style[b] = (t < 0 ? (t - l[c]) : -l[c]) + "px";
            this.lsTpc = l;
            for (var i = 0; i < bl.length - 1; i++) {
                bl[i] = bl[i + 1]
            }
            bl[i] = l;
            if (+this.cfg["delay"] > 0) {
                this.stop();
                setTimeout(function () {
                    g.run()
                }, +this.cfg["delay"])
            }
        }
    };
    this.stop = function () {
        if (this.rtprop["tmId"] != null) {
            clearInterval(this.rtprop["tmId"]);
            this.rtprop["tmId"] = null
        }
    }
};
