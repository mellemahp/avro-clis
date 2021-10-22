# Avro Cli Excecutables
Simple repo to generate releases of a avro Cli executables for generating code in different languages when using avro with bazel. It basically just uses github actions and bazel to generate a convient zip files for each languages code gen executable for use in other Bazel rules.

For more info about Avro go check out the [Avro website](https://avro.apache.org/). 

The following languages are currently building CLI's: 
- Java (uses the avro-tools jar from the avro project)
- Python (uses [avro-gen](https://github.com/rbystrit/avro_gen) with a wrapper script)