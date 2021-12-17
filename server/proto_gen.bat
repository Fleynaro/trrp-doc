python -m grpc_tools.protoc -I=../proto --python_out="./grpc" --grpc_python_out="./grpc" "../proto/*.proto"
pause