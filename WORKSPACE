workspace(name = "AvroCodeGenClis")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# ====================
# PYTHON DEPENDENCIES
# ====================
PIP_RULE_SHA = "630a7cab43a87927353efca116d20201df88fb443962bf01c7383245c7f3a623"

PIP_RULE_VERSION = "3.0.0"

http_archive(
    name = "com_github_ali5h_rules_pip",
    sha256 = PIP_RULE_SHA,
    strip_prefix = "rules_pip-%s" % PIP_RULE_VERSION,
    urls = ["https://github.com/ali5h/rules_pip/archive/%s.tar.gz" % PIP_RULE_SHA],
)

load("@com_github_ali5h_rules_pip//:defs.bzl", "pip_import")

pip_import(
    name = "pip_deps",
    python_interpreter = "python3",
    requirements = "//python:requirements.txt",
)

load("@pip_deps//:requirements.bzl", "pip_install")

pip_install()

# ==================
# JAVA DEPENDENCIES
# ==================
# import libraries from maven
RULES_JVM_EXTERNAL_TAG = "2.8"

RULES_JVM_EXTERNAL_SHA = "79c9850690d7614ecdb72d68394f994fef7534b292c4867ce5e7dec0aa7bdfad"

http_archive(
    name = "rules_jvm_external",
    sha256 = RULES_JVM_EXTERNAL_SHA,
    strip_prefix = "rules_jvm_external-%s" % RULES_JVM_EXTERNAL_TAG,
    url = "https://github.com/bazelbuild/rules_jvm_external/archive/%s.zip" % RULES_JVM_EXTERNAL_TAG,
)

load("@rules_jvm_external//:defs.bzl", "maven_install")

maven_install(
    artifacts = ["org.apache.avro:avro-tools:1.10.2"],
    repositories = ["https://repo1.maven.org/maven2"],
)
