# -*- coding: utf-8 -*-
# flake8: noqa
__all__ = ["test"]

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *

# setting scope
var = Scope(JS_BUILTINS)
set_global_object(var)

# Code follows:
var.registers(["cnonce", "CryptoJS", "getEncodePwd"])


@Js
def PyJsHoisted_cnonce_(this, arguments, var=var):
    var = Scope({"this": this, "arguments": arguments}, var)
    var.registers(["toHEX", "INT2HEX"])

    @Js
    def PyJsHoisted_toHEX_(v, this, arguments, var=var):
        var = Scope({"v": v, "this": this, "arguments": arguments}, var)
        var.registers(["h", "v"])
        var.put("h", Js(""))
        var.put(
            "h",
            var.get("INT2HEX").get(
                (PyJsBshift(var.get("v"), Js(28.0)) & Js(15))
            ),
            "+",
        )
        var.put(
            "h",
            var.get("INT2HEX").get(
                (PyJsBshift(var.get("v"), Js(24.0)) & Js(15))
            ),
            "+",
        )
        var.put(
            "h",
            var.get("INT2HEX").get(
                (PyJsBshift(var.get("v"), Js(20.0)) & Js(15))
            ),
            "+",
        )
        var.put(
            "h",
            var.get("INT2HEX").get(
                (PyJsBshift(var.get("v"), Js(16.0)) & Js(15))
            ),
            "+",
        )
        var.put(
            "h",
            var.get("INT2HEX").get(
                (PyJsBshift(var.get("v"), Js(12.0)) & Js(15))
            ),
            "+",
        )
        var.put(
            "h",
            var.get("INT2HEX").get(
                (PyJsBshift(var.get("v"), Js(8.0)) & Js(15))
            ),
            "+",
        )
        var.put(
            "h",
            var.get("INT2HEX").get(
                (PyJsBshift(var.get("v"), Js(4.0)) & Js(15))
            ),
            "+",
        )
        var.put(
            "h",
            var.get("INT2HEX").get(
                (PyJsBshift(var.get("v"), Js(0.0)) & Js(15))
            ),
            "+",
        )
        return var.get("h")

    PyJsHoisted_toHEX_.func_name = "toHEX"
    var.put("toHEX", PyJsHoisted_toHEX_)
    var.put(
        "INT2HEX",
        Js(
            [
                Js("0"),
                Js("1"),
                Js("2"),
                Js("3"),
                Js("4"),
                Js("5"),
                Js("6"),
                Js("7"),
                Js("8"),
                Js("9"),
                Js("A"),
                Js("B"),
                Js("C"),
                Js("D"),
                Js("E"),
                Js("F"),
            ]
        ),
    )
    pass
    return var.get("toHEX")(
        var.get("Math").callprop(
            "floor",
            (
                var.get("Math").callprop("random")
                * var.get("Math").callprop("pow", Js(2.0), Js(32.0))
            ),
        )
    ) + var.get("toHEX")(
        var.get("Math").callprop(
            "floor",
            (
                var.get("Math").callprop("random")
                * var.get("Math").callprop("pow", Js(2.0), Js(32.0))
            ),
        )
    )


PyJsHoisted_cnonce_.func_name = "cnonce"
var.put("cnonce", PyJsHoisted_cnonce_)


@Js
def PyJsHoisted_getEncodePwd_(pwd, this, arguments, var=var):
    var = Scope({"pwd": pwd, "this": this, "arguments": arguments}, var)
    var.registers(["pwd", "encodePwd"])
    var.put(
        "encodePwd",
        var.get("CryptoJS")
        .callprop("SHA256", var.get("pwd"))
        .callprop("toString")
        .callprop("toUpperCase"),
    )
    return var.get("encodePwd")


PyJsHoisted_getEncodePwd_.func_name = "getEncodePwd"
var.put("getEncodePwd", PyJsHoisted_getEncodePwd_)


@Js
def PyJs_anonymous_0_(h, s, this, arguments, var=var):
    var = Scope({"h": h, "s": s, "this": this, "arguments": arguments}, var)
    var.registers(
        ["t", "g", "k", "l", "s", "v", "f", "w", "h", "q", "u", "j", "x"]
    )
    var.put("f", Js({}))
    var.put("t", var.get("f").put("lib", Js({})))

    @Js
    def PyJs_anonymous_1_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers([])
        pass

    PyJs_anonymous_1_._set_name("anonymous")
    var.put("g", PyJs_anonymous_1_)

    @Js
    def PyJs_anonymous_2_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a", "c"])
        var.get("g").put("prototype", var.get("this"))
        var.put("c", var.get("g").create())
        (var.get("a") and var.get("c").callprop("mixIn", var.get("a")))

        @Js
        def PyJs_anonymous_3_(this, arguments, var=var):
            var = Scope({"this": this, "arguments": arguments}, var)
            var.registers([])
            var.get("c").get("$super").get("init").callprop(
                "apply", var.get("this"), var.get("arguments")
            )

        PyJs_anonymous_3_._set_name("anonymous")
        (
            var.get("c").callprop("hasOwnProperty", Js("init"))
            or var.get("c").put("init", PyJs_anonymous_3_)
        )
        var.get("c").get("init").put("prototype", var.get("c"))
        var.get("c").put("$super", var.get("this"))
        return var.get("c")

    PyJs_anonymous_2_._set_name("anonymous")

    @Js
    def PyJs_anonymous_4_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers(["a"])
        var.put("a", var.get("this").callprop("extend"))
        var.get("a").get("init").callprop(
            "apply", var.get("a"), var.get("arguments")
        )
        return var.get("a")

    PyJs_anonymous_4_._set_name("anonymous")

    @Js
    def PyJs_anonymous_5_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers([])
        pass

    PyJs_anonymous_5_._set_name("anonymous")

    @Js
    def PyJs_anonymous_6_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a", "c"])
        for PyJsTemp in var.get("a"):
            var.put("c", PyJsTemp)
            (
                var.get("a").callprop("hasOwnProperty", var.get("c"))
                and var.get("this").put(
                    var.get("c"), var.get("a").get(var.get("c"))
                )
            )
        (
            var.get("a").callprop("hasOwnProperty", Js("toString"))
            and var.get("this").put("toString", var.get("a").get("toString"))
        )

    PyJs_anonymous_6_._set_name("anonymous")

    @Js
    def PyJs_anonymous_7_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers([])
        return (
            var.get("this")
            .get("init")
            .get("prototype")
            .callprop("extend", var.get("this"))
        )

    PyJs_anonymous_7_._set_name("anonymous")
    var.put(
        "j",
        var.get("t").put(
            "Base",
            Js(
                {
                    "extend": PyJs_anonymous_2_,
                    "create": PyJs_anonymous_4_,
                    "init": PyJs_anonymous_5_,
                    "mixIn": PyJs_anonymous_6_,
                    "clone": PyJs_anonymous_7_,
                }
            ),
        ),
    )

    @Js
    def PyJs_anonymous_8_(a, c, this, arguments, var=var):
        var = Scope(
            {"a": a, "c": c, "this": this, "arguments": arguments}, var
        )
        var.registers(["a", "c"])
        var.put("a", var.get("this").put("words", (var.get("a") or Js([]))))
        var.get("this").put(
            "sigBytes",
            (
                var.get("c")
                if (var.get("c") != var.get("s"))
                else (Js(4.0) * var.get("a").get("length"))
            ),
        )

    PyJs_anonymous_8_._set_name("anonymous")

    @Js
    def PyJs_anonymous_9_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])
        return (var.get("a") or var.get("u")).callprop(
            "stringify", var.get("this")
        )

    PyJs_anonymous_9_._set_name("anonymous")

    @Js
    def PyJs_anonymous_10_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a", "b", "c", "d", "e"])
        var.put("c", var.get("this").get("words"))
        var.put("d", var.get("a").get("words"))
        var.put("b", var.get("this").get("sigBytes"))
        var.put("a", var.get("a").get("sigBytes"))
        var.get("this").callprop("clamp")
        if var.get("b") % Js(4.0):
            # for JS loop
            var.put("e", Js(0.0))
            while var.get("e") < var.get("a"):
                try:
                    var.get("c").put(
                        PyJsBshift((var.get("b") + var.get("e")), Js(2.0)),
                        (
                            (
                                PyJsBshift(
                                    var.get("d").get(
                                        PyJsBshift(var.get("e"), Js(2.0))
                                    ),
                                    (
                                        Js(24.0)
                                        - (Js(8.0) * (var.get("e") % Js(4.0)))
                                    ),
                                )
                                & Js(255.0)
                            )
                            << (
                                Js(24.0)
                                - (
                                    Js(8.0)
                                    * ((var.get("b") + var.get("e")) % Js(4.0))
                                )
                            )
                        ),
                        "|",
                    )
                finally:
                    (
                        var.put("e", Js(var.get("e").to_number()) + Js(1))
                        - Js(1)
                    )
        else:
            if Js(65535.0) < var.get("d").get("length"):
                # for JS loop
                var.put("e", Js(0.0))
                while var.get("e") < var.get("a"):
                    try:
                        var.get("c").put(
                            PyJsBshift((var.get("b") + var.get("e")), Js(2.0)),
                            var.get("d").get(
                                PyJsBshift(var.get("e"), Js(2.0))
                            ),
                        )
                    finally:
                        var.put("e", Js(4.0), "+")
            else:
                var.get("c").get("push").callprop(
                    "apply", var.get("c"), var.get("d")
                )
        var.get("this").put("sigBytes", var.get("a"), "+")
        return var.get("this")

    PyJs_anonymous_10_._set_name("anonymous")

    @Js
    def PyJs_anonymous_11_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers(["a", "c"])
        var.put("a", var.get("this").get("words"))
        var.put("c", var.get("this").get("sigBytes"))
        var.get("a").put(
            PyJsBshift(var.get("c"), Js(2.0)),
            (
                Js(4294967295.0)
                << (Js(32.0) - (Js(8.0) * (var.get("c") % Js(4.0))))
            ),
            "&",
        )
        var.get("a").put(
            "length", var.get("h").callprop("ceil", (var.get("c") / Js(4.0)))
        )

    PyJs_anonymous_11_._set_name("anonymous")

    @Js
    def PyJs_anonymous_12_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers(["a"])
        var.put(
            "a", var.get("j").get("clone").callprop("call", var.get("this"))
        )
        var.get("a").put(
            "words", var.get("this").get("words").callprop("slice", Js(0.0))
        )
        return var.get("a")

    PyJs_anonymous_12_._set_name("anonymous")

    @Js
    def PyJs_anonymous_13_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["d", "a", "c"])
        # for JS loop
        var.put("c", Js([]))
        var.put("d", Js(0.0))
        while var.get("d") < var.get("a"):
            try:
                var.get("c").callprop(
                    "push",
                    (
                        (Js(4294967296.0) * var.get("h").callprop("random"))
                        | Js(0.0)
                    ),
                )
            finally:
                var.put("d", Js(4.0), "+")
        return var.get("q").get("init").create(var.get("c"), var.get("a"))

    PyJs_anonymous_13_._set_name("anonymous")
    var.put(
        "q",
        var.get("t").put(
            "WordArray",
            var.get("j").callprop(
                "extend",
                Js(
                    {
                        "init": PyJs_anonymous_8_,
                        "toString": PyJs_anonymous_9_,
                        "concat": PyJs_anonymous_10_,
                        "clamp": PyJs_anonymous_11_,
                        "clone": PyJs_anonymous_12_,
                        "random": PyJs_anonymous_13_,
                    }
                ),
            ),
        ),
    )
    var.put("v", var.get("f").put("enc", Js({})))

    @Js
    def PyJs_anonymous_14_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a", "b", "c", "d", "e"])
        var.put("c", var.get("a").get("words"))
        var.put("a", var.get("a").get("sigBytes"))
        # for JS loop
        var.put("d", Js([]))
        var.put("b", Js(0.0))
        while var.get("b") < var.get("a"):
            try:
                var.put(
                    "e",
                    (
                        PyJsBshift(
                            var.get("c").get(
                                PyJsBshift(var.get("b"), Js(2.0))
                            ),
                            (Js(24.0) - (Js(8.0) * (var.get("b") % Js(4.0)))),
                        )
                        & Js(255.0)
                    ),
                )
                var.get("d").callprop(
                    "push",
                    PyJsBshift(var.get("e"), Js(4.0)).callprop(
                        "toString", Js(16.0)
                    ),
                )
                var.get("d").callprop(
                    "push",
                    (var.get("e") & Js(15.0)).callprop("toString", Js(16.0)),
                )
            finally:
                (var.put("b", Js(var.get("b").to_number()) + Js(1)) - Js(1))
        return var.get("d").callprop("join", Js(""))

    PyJs_anonymous_14_._set_name("anonymous")

    @Js
    def PyJs_anonymous_15_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["d", "a", "c", "b"])
        # for JS loop
        var.put("c", var.get("a").get("length"))
        var.put("d", Js([]))
        var.put("b", Js(0.0))
        while var.get("b") < var.get("c"):
            try:
                var.get("d").put(
                    PyJsBshift(var.get("b"), Js(3.0)),
                    (
                        var.get("parseInt")(
                            var.get("a").callprop(
                                "substr", var.get("b"), Js(2.0)
                            ),
                            Js(16.0),
                        )
                        << (Js(24.0) - (Js(4.0) * (var.get("b") % Js(8.0))))
                    ),
                    "|",
                )
            finally:
                var.put("b", Js(2.0), "+")
        return (
            var.get("q")
            .get("init")
            .create(var.get("d"), (var.get("c") / Js(2.0)))
        )

    PyJs_anonymous_15_._set_name("anonymous")
    var.put(
        "u",
        var.get("v").put(
            "Hex",
            Js({"stringify": PyJs_anonymous_14_, "parse": PyJs_anonymous_15_}),
        ),
    )

    @Js
    def PyJs_anonymous_16_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["d", "a", "c", "b"])
        var.put("c", var.get("a").get("words"))
        var.put("a", var.get("a").get("sigBytes"))
        # for JS loop
        var.put("d", Js([]))
        var.put("b", Js(0.0))
        while var.get("b") < var.get("a"):
            try:
                var.get("d").callprop(
                    "push",
                    var.get("String").callprop(
                        "fromCharCode",
                        (
                            PyJsBshift(
                                var.get("c").get(
                                    PyJsBshift(var.get("b"), Js(2.0))
                                ),
                                (
                                    Js(24.0)
                                    - (Js(8.0) * (var.get("b") % Js(4.0)))
                                ),
                            )
                            & Js(255.0)
                        ),
                    ),
                )
            finally:
                (var.put("b", Js(var.get("b").to_number()) + Js(1)) - Js(1))
        return var.get("d").callprop("join", Js(""))

    PyJs_anonymous_16_._set_name("anonymous")

    @Js
    def PyJs_anonymous_17_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["d", "a", "c", "b"])
        # for JS loop
        var.put("c", var.get("a").get("length"))
        var.put("d", Js([]))
        var.put("b", Js(0.0))
        while var.get("b") < var.get("c"):
            try:
                var.get("d").put(
                    PyJsBshift(var.get("b"), Js(2.0)),
                    (
                        (
                            var.get("a").callprop("charCodeAt", var.get("b"))
                            & Js(255.0)
                        )
                        << (Js(24.0) - (Js(8.0) * (var.get("b") % Js(4.0))))
                    ),
                    "|",
                )
            finally:
                (var.put("b", Js(var.get("b").to_number()) + Js(1)) - Js(1))
        return var.get("q").get("init").create(var.get("d"), var.get("c"))

    PyJs_anonymous_17_._set_name("anonymous")
    var.put(
        "k",
        var.get("v").put(
            "Latin1",
            Js({"stringify": PyJs_anonymous_16_, "parse": PyJs_anonymous_17_}),
        ),
    )

    @Js
    def PyJs_anonymous_18_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])
        try:
            return var.get("decodeURIComponent")(
                var.get("escape")(
                    var.get("k").callprop("stringify", var.get("a"))
                )
            )
        except PyJsException as PyJsTempException:
            PyJsHolder_63_93562790 = var.own.get("c")
            var.force_own_put("c", PyExceptionToJs(PyJsTempException))
            try:
                PyJsTempException = JsToPyException(
                    var.get("Error")(Js("Malformed UTF-8 data"))
                )
                raise PyJsTempException
            finally:
                if PyJsHolder_63_93562790 is not None:
                    var.own["c"] = PyJsHolder_63_93562790
                else:
                    del var.own["c"]
                del PyJsHolder_63_93562790

    PyJs_anonymous_18_._set_name("anonymous")

    @Js
    def PyJs_anonymous_19_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])
        return var.get("k").callprop(
            "parse",
            var.get("unescape")(var.get("encodeURIComponent")(var.get("a"))),
        )

    PyJs_anonymous_19_._set_name("anonymous")
    var.put(
        "l",
        var.get("v").put(
            "Utf8",
            Js({"stringify": PyJs_anonymous_18_, "parse": PyJs_anonymous_19_}),
        ),
    )

    @Js
    def PyJs_anonymous_20_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers([])
        var.get("this").put("_data", var.get("q").get("init").create())
        var.get("this").put("_nDataBytes", Js(0.0))

    PyJs_anonymous_20_._set_name("anonymous")

    @Js
    def PyJs_anonymous_21_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])
        (
            (Js("string") == var.get("a", throw=False).typeof())
            and var.put("a", var.get("l").callprop("parse", var.get("a")))
        )
        var.get("this").get("_data").callprop("concat", var.get("a"))
        var.get("this").put("_nDataBytes", var.get("a").get("sigBytes"), "+")

    PyJs_anonymous_21_._set_name("anonymous")

    @Js
    def PyJs_anonymous_22_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a", "m", "b", "f", "c", "d", "e"])
        var.put("c", var.get("this").get("_data"))
        var.put("d", var.get("c").get("words"))
        var.put("b", var.get("c").get("sigBytes"))
        var.put("e", var.get("this").get("blockSize"))
        var.put("f", (var.get("b") / (Js(4.0) * var.get("e"))))
        var.put(
            "f",
            (
                var.get("h").callprop("ceil", var.get("f"))
                if var.get("a")
                else var.get("h").callprop(
                    "max",
                    (
                        (var.get("f") | Js(0.0))
                        - var.get("this").get("_minBufferSize")
                    ),
                    Js(0.0),
                )
            ),
        )
        var.put("a", (var.get("f") * var.get("e")))
        var.put(
            "b",
            var.get("h").callprop(
                "min", (Js(4.0) * var.get("a")), var.get("b")
            ),
        )
        if var.get("a"):
            # for JS loop
            var.put("m", Js(0.0))
            while var.get("m") < var.get("a"):
                try:
                    var.get("this").callprop(
                        "_doProcessBlock", var.get("d"), var.get("m")
                    )
                finally:
                    var.put("m", var.get("e"), "+")
            var.put(
                "m", var.get("d").callprop("splice", Js(0.0), var.get("a"))
            )
            var.get("c").put("sigBytes", var.get("b"), "-")
        return var.get("q").get("init").create(var.get("m"), var.get("b"))

    PyJs_anonymous_22_._set_name("anonymous")

    @Js
    def PyJs_anonymous_23_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers(["a"])
        var.put(
            "a", var.get("j").get("clone").callprop("call", var.get("this"))
        )
        var.get("a").put(
            "_data", var.get("this").get("_data").callprop("clone")
        )
        return var.get("a")

    PyJs_anonymous_23_._set_name("anonymous")
    var.put(
        "x",
        var.get("t").put(
            "BufferedBlockAlgorithm",
            var.get("j").callprop(
                "extend",
                Js(
                    {
                        "reset": PyJs_anonymous_20_,
                        "_append": PyJs_anonymous_21_,
                        "_process": PyJs_anonymous_22_,
                        "clone": PyJs_anonymous_23_,
                        "_minBufferSize": Js(0.0),
                    }
                ),
            ),
        ),
    )

    @Js
    def PyJs_anonymous_24_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])
        var.get("this").put(
            "cfg", var.get("this").get("cfg").callprop("extend", var.get("a"))
        )
        var.get("this").callprop("reset")

    PyJs_anonymous_24_._set_name("anonymous")

    @Js
    def PyJs_anonymous_25_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers([])
        var.get("x").get("reset").callprop("call", var.get("this"))
        var.get("this").callprop("_doReset")

    PyJs_anonymous_25_._set_name("anonymous")

    @Js
    def PyJs_anonymous_26_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])
        var.get("this").callprop("_append", var.get("a"))
        var.get("this").callprop("_process")
        return var.get("this")

    PyJs_anonymous_26_._set_name("anonymous")

    @Js
    def PyJs_anonymous_27_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])
        (var.get("a") and var.get("this").callprop("_append", var.get("a")))
        return var.get("this").callprop("_doFinalize")

    PyJs_anonymous_27_._set_name("anonymous")

    @Js
    def PyJs_anonymous_28_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])

        @Js
        def PyJs_anonymous_29_(c, d, this, arguments, var=var):
            var = Scope(
                {"c": c, "d": d, "this": this, "arguments": arguments}, var
            )
            var.registers(["d", "c"])
            return (
                var.get("a")
                .get("init")
                .create(var.get("d"))
                .callprop("finalize", var.get("c"))
            )

        PyJs_anonymous_29_._set_name("anonymous")
        return PyJs_anonymous_29_

    PyJs_anonymous_28_._set_name("anonymous")

    @Js
    def PyJs_anonymous_30_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])

        @Js
        def PyJs_anonymous_31_(c, d, this, arguments, var=var):
            var = Scope(
                {"c": c, "d": d, "this": this, "arguments": arguments}, var
            )
            var.registers(["d", "c"])
            return (
                var.get("w")
                .get("HMAC")
                .get("init")
                .create(var.get("a"), var.get("d"))
                .callprop("finalize", var.get("c"))
            )

        PyJs_anonymous_31_._set_name("anonymous")
        return PyJs_anonymous_31_

    PyJs_anonymous_30_._set_name("anonymous")
    var.get("t").put(
        "Hasher",
        var.get("x").callprop(
            "extend",
            Js(
                {
                    "cfg": var.get("j").callprop("extend"),
                    "init": PyJs_anonymous_24_,
                    "reset": PyJs_anonymous_25_,
                    "update": PyJs_anonymous_26_,
                    "finalize": PyJs_anonymous_27_,
                    "blockSize": Js(16.0),
                    "_createHelper": PyJs_anonymous_28_,
                    "_createHmacHelper": PyJs_anonymous_30_,
                }
            ),
        ),
    )
    var.put("w", var.get("f").put("algo", Js({})))
    return var.get("f")


PyJs_anonymous_0_._set_name("anonymous")
var.put(
    "CryptoJS", (var.get("CryptoJS") or PyJs_anonymous_0_(var.get("Math")))
)


@Js
def PyJs_anonymous_32_(h, this, arguments, var=var):
    var = Scope({"h": h, "this": this, "arguments": arguments}, var)
    var.registers(
        ["t", "a", "g", "u", "k", "l", "v", "f", "w", "h", "q", "s", "j", "x"]
    )
    # for JS loop
    var.put("s", var.get("CryptoJS"))
    var.put("f", var.get("s").get("lib"))
    var.put("t", var.get("f").get("WordArray"))
    var.put("g", var.get("f").get("Hasher"))
    var.put("f", var.get("s").get("algo"))
    var.put("j", Js([]))
    var.put("q", Js([]))

    @Js
    def PyJs_anonymous_33_(a, this, arguments, var=var):
        var = Scope({"a": a, "this": this, "arguments": arguments}, var)
        var.registers(["a"])
        return (
            Js(4294967296.0) * (var.get("a") - (var.get("a") | Js(0.0)))
        ) | Js(0.0)

    PyJs_anonymous_33_._set_name("anonymous")
    var.put("v", PyJs_anonymous_33_)
    var.put("u", Js(2.0))
    var.put("k", Js(0.0))
    while Js(64.0) > var.get("k"):
        pass

        class JS_BREAK_LABEL_61(Exception):
            pass

        try:
            var.put("l", var.get("u"))
            # for JS loop
            var.put("x", var.get("h").callprop("sqrt", var.get("l")))
            var.put("w", Js(2.0))
            while var.get("w") <= var.get("x"):
                try:
                    if (var.get("l") % var.get("w")).neg():
                        var.put("l", Js(1.0).neg())
                        raise JS_BREAK_LABEL_61("Breaked")
                finally:
                    (
                        var.put("w", Js(var.get("w").to_number()) + Js(1))
                        - Js(1)
                    )
            var.put("l", Js(0.0).neg())
        except JS_BREAK_LABEL_61:
            pass
        (
            var.get("l")
            and PyJsComma(
                PyJsComma(
                    (
                        (Js(8.0) > var.get("k"))
                        and var.get("j").put(
                            var.get("k"),
                            var.get("v")(
                                var.get("h").callprop(
                                    "pow", var.get("u"), Js(0.5)
                                )
                            ),
                        )
                    ),
                    var.get("q").put(
                        var.get("k"),
                        var.get("v")(
                            var.get("h").callprop(
                                "pow", var.get("u"), (Js(1.0) / Js(3.0))
                            )
                        ),
                    ),
                ),
                (var.put("k", Js(var.get("k").to_number()) + Js(1)) - Js(1)),
            )
        )
        (var.put("u", Js(var.get("u").to_number()) + Js(1)) - Js(1))

    var.put("a", Js([]))

    @Js
    def PyJs_anonymous_34_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers([])
        var.get("this").put(
            "_hash",
            var.get("t")
            .get("init")
            .create(var.get("j").callprop("slice", Js(0.0))),
        )

    PyJs_anonymous_34_._set_name("anonymous")

    @Js
    def PyJs_anonymous_35_(c, d, this, arguments, var=var):
        var = Scope(
            {"c": c, "d": d, "this": this, "arguments": arguments}, var
        )
        var.registers(
            [
                "p",
                "n",
                "k",
                "l",
                "g",
                "m",
                "b",
                "f",
                "c",
                "h",
                "d",
                "r",
                "e",
                "j",
            ]
        )
        # for JS loop
        var.put("b", var.get("this").get("_hash").get("words"))
        var.put("e", var.get("b").get("0"))
        var.put("f", var.get("b").get("1"))
        var.put("m", var.get("b").get("2"))
        var.put("h", var.get("b").get("3"))
        var.put("p", var.get("b").get("4"))
        var.put("j", var.get("b").get("5"))
        var.put("k", var.get("b").get("6"))
        var.put("l", var.get("b").get("7"))
        var.put("n", Js(0.0))
        while Js(64.0) > var.get("n"):
            try:
                if Js(16.0) > var.get("n"):
                    var.get("a").put(
                        var.get("n"),
                        (
                            var.get("c").get((var.get("d") + var.get("n")))
                            | Js(0.0)
                        ),
                    )
                else:
                    var.put("r", var.get("a").get((var.get("n") - Js(15.0))))
                    var.put("g", var.get("a").get((var.get("n") - Js(2.0))))

                    def PyJs_LONG_36_(var=var):
                        return (
                            (
                                (
                                    (
                                        (
                                            (var.get("r") << Js(25.0))
                                            | PyJsBshift(var.get("r"), Js(7.0))
                                        )
                                        ^ (
                                            (var.get("r") << Js(14.0))
                                            | PyJsBshift(
                                                var.get("r"), Js(18.0)
                                            )
                                        )
                                    )
                                    ^ PyJsBshift(var.get("r"), Js(3.0))
                                )
                                + var.get("a").get((var.get("n") - Js(7.0)))
                            )
                            + (
                                (
                                    (
                                        (var.get("g") << Js(15.0))
                                        | PyJsBshift(var.get("g"), Js(17.0))
                                    )
                                    ^ (
                                        (var.get("g") << Js(13.0))
                                        | PyJsBshift(var.get("g"), Js(19.0))
                                    )
                                )
                                ^ PyJsBshift(var.get("g"), Js(10.0))
                            )
                        ) + var.get("a").get((var.get("n") - Js(16.0)))

                    var.get("a").put(var.get("n"), PyJs_LONG_36_())
                var.put(
                    "r",
                    (
                        (
                            (
                                (
                                    var.get("l")
                                    + (
                                        (
                                            (
                                                (var.get("p") << Js(26.0))
                                                | PyJsBshift(
                                                    var.get("p"), Js(6.0)
                                                )
                                            )
                                            ^ (
                                                (var.get("p") << Js(21.0))
                                                | PyJsBshift(
                                                    var.get("p"), Js(11.0)
                                                )
                                            )
                                        )
                                        ^ (
                                            (var.get("p") << Js(7.0))
                                            | PyJsBshift(
                                                var.get("p"), Js(25.0)
                                            )
                                        )
                                    )
                                )
                                + (
                                    (var.get("p") & var.get("j"))
                                    ^ ((~var.get("p")) & var.get("k"))
                                )
                            )
                            + var.get("q").get(var.get("n"))
                        )
                        + var.get("a").get(var.get("n"))
                    ),
                )
                var.put(
                    "g",
                    (
                        (
                            (
                                (
                                    (var.get("e") << Js(30.0))
                                    | PyJsBshift(var.get("e"), Js(2.0))
                                )
                                ^ (
                                    (var.get("e") << Js(19.0))
                                    | PyJsBshift(var.get("e"), Js(13.0))
                                )
                            )
                            ^ (
                                (var.get("e") << Js(10.0))
                                | PyJsBshift(var.get("e"), Js(22.0))
                            )
                        )
                        + (
                            (
                                (var.get("e") & var.get("f"))
                                ^ (var.get("e") & var.get("m"))
                            )
                            ^ (var.get("f") & var.get("m"))
                        )
                    ),
                )
                var.put("l", var.get("k"))
                var.put("k", var.get("j"))
                var.put("j", var.get("p"))
                var.put("p", ((var.get("h") + var.get("r")) | Js(0.0)))
                var.put("h", var.get("m"))
                var.put("m", var.get("f"))
                var.put("f", var.get("e"))
                var.put("e", ((var.get("r") + var.get("g")) | Js(0.0)))
            finally:
                (var.put("n", Js(var.get("n").to_number()) + Js(1)) - Js(1))
        var.get("b").put(
            "0", ((var.get("b").get("0") + var.get("e")) | Js(0.0))
        )
        var.get("b").put(
            "1", ((var.get("b").get("1") + var.get("f")) | Js(0.0))
        )
        var.get("b").put(
            "2", ((var.get("b").get("2") + var.get("m")) | Js(0.0))
        )
        var.get("b").put(
            "3", ((var.get("b").get("3") + var.get("h")) | Js(0.0))
        )
        var.get("b").put(
            "4", ((var.get("b").get("4") + var.get("p")) | Js(0.0))
        )
        var.get("b").put(
            "5", ((var.get("b").get("5") + var.get("j")) | Js(0.0))
        )
        var.get("b").put(
            "6", ((var.get("b").get("6") + var.get("k")) | Js(0.0))
        )
        var.get("b").put(
            "7", ((var.get("b").get("7") + var.get("l")) | Js(0.0))
        )

    PyJs_anonymous_35_._set_name("anonymous")

    @Js
    def PyJs_anonymous_37_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers(["d", "a", "e", "b"])
        var.put("a", var.get("this").get("_data"))
        var.put("d", var.get("a").get("words"))
        var.put("b", (Js(8.0) * var.get("this").get("_nDataBytes")))
        var.put("e", (Js(8.0) * var.get("a").get("sigBytes")))
        var.get("d").put(
            PyJsBshift(var.get("e"), Js(5.0)),
            (Js(128.0) << (Js(24.0) - (var.get("e") % Js(32.0)))),
            "|",
        )
        var.get("d").put(
            (
                (PyJsBshift((var.get("e") + Js(64.0)), Js(9.0)) << Js(4.0))
                + Js(14.0)
            ),
            var.get("h").callprop("floor", (var.get("b") / Js(4294967296.0))),
        )
        var.get("d").put(
            (
                (PyJsBshift((var.get("e") + Js(64.0)), Js(9.0)) << Js(4.0))
                + Js(15.0)
            ),
            var.get("b"),
        )
        var.get("a").put("sigBytes", (Js(4.0) * var.get("d").get("length")))
        var.get("this").callprop("_process")
        return var.get("this").get("_hash")

    PyJs_anonymous_37_._set_name("anonymous")

    @Js
    def PyJs_anonymous_38_(this, arguments, var=var):
        var = Scope({"this": this, "arguments": arguments}, var)
        var.registers(["a"])
        var.put(
            "a", var.get("g").get("clone").callprop("call", var.get("this"))
        )
        var.get("a").put(
            "_hash", var.get("this").get("_hash").callprop("clone")
        )
        var.get("returna")

    PyJs_anonymous_38_._set_name("anonymous")
    var.put(
        "f",
        var.get("f").put(
            "SHA256",
            var.get("g").callprop(
                "extend",
                Js(
                    {
                        "_doReset": PyJs_anonymous_34_,
                        "_doProcessBlock": PyJs_anonymous_35_,
                        "_doFinalize": PyJs_anonymous_37_,
                        "clone": PyJs_anonymous_38_,
                    }
                ),
            ),
        ),
    )
    var.get("s").put(
        "SHA256", var.get("g").callprop("_createHelper", var.get("f"))
    )
    var.get("s").put(
        "HmacSHA256", var.get("g").callprop("_createHmacHelper", var.get("f"))
    )


PyJs_anonymous_32_._set_name("anonymous")
PyJs_anonymous_32_(var.get("Math"))
pass
pass
pass


# Add lib to the module scope
test = var.to_python()
