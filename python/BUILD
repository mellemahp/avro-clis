load("@pip_deps//:requirements.bzl", "requirement")

py_binary(
    name = "cli_binary",
    srcs = ["wrapper.py"],
    main = "wrapper.py",
    visibility = ["//visibility:public"],
    deps = [
        requirement("avro-gen"),
    ],
)
