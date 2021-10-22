genrule(
    name = "release",
    srcs = ["avro_cli_java_executable_deploy.jar"],
    outs = ["avro_cli.jar"],
    cmd = "cp $(location avro_cli_java_executable_deploy.jar) $@",
    visibility = ["//visibility:public"],
)

java_binary(
    name = "avro_cli_java_executable",
    main_class = "org.apache.avro.tool.Main",
    runtime_deps = [
        "@maven//:org_apache_avro_avro_tools",
    ],
)
