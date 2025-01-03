# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tei_pb2 as tei__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in tei_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class InfoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Info = channel.unary_unary(
            '/tei.v1.Info/Info',
            request_serializer=tei__pb2.InfoRequest.SerializeToString,
            response_deserializer=tei__pb2.InfoResponse.FromString,
            _registered_method=True)


class InfoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InfoServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Info': grpc.unary_unary_rpc_method_handler(
            servicer.Info,
            request_deserializer=tei__pb2.InfoRequest.FromString,
            response_serializer=tei__pb2.InfoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'tei.v1.Info', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('tei.v1.Info', rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Info(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Info(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tei.v1.Info/Info',
            tei__pb2.InfoRequest.SerializeToString,
            tei__pb2.InfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class EmbedStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Embed = channel.unary_unary(
            '/tei.v1.Embed/Embed',
            request_serializer=tei__pb2.EmbedRequest.SerializeToString,
            response_deserializer=tei__pb2.EmbedResponse.FromString,
            _registered_method=True)
        self.EmbedStream = channel.stream_stream(
            '/tei.v1.Embed/EmbedStream',
            request_serializer=tei__pb2.EmbedRequest.SerializeToString,
            response_deserializer=tei__pb2.EmbedResponse.FromString,
            _registered_method=True)
        self.EmbedSparse = channel.unary_unary(
            '/tei.v1.Embed/EmbedSparse',
            request_serializer=tei__pb2.EmbedSparseRequest.SerializeToString,
            response_deserializer=tei__pb2.EmbedSparseResponse.FromString,
            _registered_method=True)
        self.EmbedSparseStream = channel.stream_stream(
            '/tei.v1.Embed/EmbedSparseStream',
            request_serializer=tei__pb2.EmbedSparseRequest.SerializeToString,
            response_deserializer=tei__pb2.EmbedSparseResponse.FromString,
            _registered_method=True)
        self.EmbedAll = channel.unary_unary(
            '/tei.v1.Embed/EmbedAll',
            request_serializer=tei__pb2.EmbedAllRequest.SerializeToString,
            response_deserializer=tei__pb2.EmbedAllResponse.FromString,
            _registered_method=True)
        self.EmbedAllStream = channel.stream_stream(
            '/tei.v1.Embed/EmbedAllStream',
            request_serializer=tei__pb2.EmbedAllRequest.SerializeToString,
            response_deserializer=tei__pb2.EmbedAllResponse.FromString,
            _registered_method=True)


class EmbedServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Embed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EmbedStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EmbedSparse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EmbedSparseStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EmbedAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EmbedAllStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmbedServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Embed': grpc.unary_unary_rpc_method_handler(
            servicer.Embed,
            request_deserializer=tei__pb2.EmbedRequest.FromString,
            response_serializer=tei__pb2.EmbedResponse.SerializeToString,
        ),
        'EmbedStream': grpc.stream_stream_rpc_method_handler(
            servicer.EmbedStream,
            request_deserializer=tei__pb2.EmbedRequest.FromString,
            response_serializer=tei__pb2.EmbedResponse.SerializeToString,
        ),
        'EmbedSparse': grpc.unary_unary_rpc_method_handler(
            servicer.EmbedSparse,
            request_deserializer=tei__pb2.EmbedSparseRequest.FromString,
            response_serializer=tei__pb2.EmbedSparseResponse.SerializeToString,
        ),
        'EmbedSparseStream': grpc.stream_stream_rpc_method_handler(
            servicer.EmbedSparseStream,
            request_deserializer=tei__pb2.EmbedSparseRequest.FromString,
            response_serializer=tei__pb2.EmbedSparseResponse.SerializeToString,
        ),
        'EmbedAll': grpc.unary_unary_rpc_method_handler(
            servicer.EmbedAll,
            request_deserializer=tei__pb2.EmbedAllRequest.FromString,
            response_serializer=tei__pb2.EmbedAllResponse.SerializeToString,
        ),
        'EmbedAllStream': grpc.stream_stream_rpc_method_handler(
            servicer.EmbedAllStream,
            request_deserializer=tei__pb2.EmbedAllRequest.FromString,
            response_serializer=tei__pb2.EmbedAllResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'tei.v1.Embed', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('tei.v1.Embed', rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Embed(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Embed(request,
              target,
              options=(),
              channel_credentials=None,
              call_credentials=None,
              insecure=False,
              compression=None,
              wait_for_ready=None,
              timeout=None,
              metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tei.v1.Embed/Embed',
            tei__pb2.EmbedRequest.SerializeToString,
            tei__pb2.EmbedResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EmbedStream(request_iterator,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/tei.v1.Embed/EmbedStream',
            tei__pb2.EmbedRequest.SerializeToString,
            tei__pb2.EmbedResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EmbedSparse(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tei.v1.Embed/EmbedSparse',
            tei__pb2.EmbedSparseRequest.SerializeToString,
            tei__pb2.EmbedSparseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EmbedSparseStream(request_iterator,
                          target,
                          options=(),
                          channel_credentials=None,
                          call_credentials=None,
                          insecure=False,
                          compression=None,
                          wait_for_ready=None,
                          timeout=None,
                          metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/tei.v1.Embed/EmbedSparseStream',
            tei__pb2.EmbedSparseRequest.SerializeToString,
            tei__pb2.EmbedSparseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EmbedAll(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tei.v1.Embed/EmbedAll',
            tei__pb2.EmbedAllRequest.SerializeToString,
            tei__pb2.EmbedAllResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EmbedAllStream(request_iterator,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/tei.v1.Embed/EmbedAllStream',
            tei__pb2.EmbedAllRequest.SerializeToString,
            tei__pb2.EmbedAllResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class PredictStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Predict = channel.unary_unary(
            '/tei.v1.Predict/Predict',
            request_serializer=tei__pb2.PredictRequest.SerializeToString,
            response_deserializer=tei__pb2.PredictResponse.FromString,
            _registered_method=True)
        self.PredictPair = channel.unary_unary(
            '/tei.v1.Predict/PredictPair',
            request_serializer=tei__pb2.PredictPairRequest.SerializeToString,
            response_deserializer=tei__pb2.PredictResponse.FromString,
            _registered_method=True)
        self.PredictStream = channel.stream_stream(
            '/tei.v1.Predict/PredictStream',
            request_serializer=tei__pb2.PredictRequest.SerializeToString,
            response_deserializer=tei__pb2.PredictResponse.FromString,
            _registered_method=True)
        self.PredictPairStream = channel.stream_stream(
            '/tei.v1.Predict/PredictPairStream',
            request_serializer=tei__pb2.PredictPairRequest.SerializeToString,
            response_deserializer=tei__pb2.PredictResponse.FromString,
            _registered_method=True)


class PredictServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PredictPair(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PredictStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PredictPairStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PredictServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Predict': grpc.unary_unary_rpc_method_handler(
            servicer.Predict,
            request_deserializer=tei__pb2.PredictRequest.FromString,
            response_serializer=tei__pb2.PredictResponse.SerializeToString,
        ),
        'PredictPair': grpc.unary_unary_rpc_method_handler(
            servicer.PredictPair,
            request_deserializer=tei__pb2.PredictPairRequest.FromString,
            response_serializer=tei__pb2.PredictResponse.SerializeToString,
        ),
        'PredictStream': grpc.stream_stream_rpc_method_handler(
            servicer.PredictStream,
            request_deserializer=tei__pb2.PredictRequest.FromString,
            response_serializer=tei__pb2.PredictResponse.SerializeToString,
        ),
        'PredictPairStream': grpc.stream_stream_rpc_method_handler(
            servicer.PredictPairStream,
            request_deserializer=tei__pb2.PredictPairRequest.FromString,
            response_serializer=tei__pb2.PredictResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'tei.v1.Predict', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('tei.v1.Predict', rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Predict(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Predict(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tei.v1.Predict/Predict',
            tei__pb2.PredictRequest.SerializeToString,
            tei__pb2.PredictResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PredictPair(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tei.v1.Predict/PredictPair',
            tei__pb2.PredictPairRequest.SerializeToString,
            tei__pb2.PredictResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PredictStream(request_iterator,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/tei.v1.Predict/PredictStream',
            tei__pb2.PredictRequest.SerializeToString,
            tei__pb2.PredictResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PredictPairStream(request_iterator,
                          target,
                          options=(),
                          channel_credentials=None,
                          call_credentials=None,
                          insecure=False,
                          compression=None,
                          wait_for_ready=None,
                          timeout=None,
                          metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/tei.v1.Predict/PredictPairStream',
            tei__pb2.PredictPairRequest.SerializeToString,
            tei__pb2.PredictResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class RerankStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Rerank = channel.unary_unary(
            '/tei.v1.Rerank/Rerank',
            request_serializer=tei__pb2.RerankRequest.SerializeToString,
            response_deserializer=tei__pb2.RerankResponse.FromString,
            _registered_method=True)
        self.RerankStream = channel.stream_unary(
            '/tei.v1.Rerank/RerankStream',
            request_serializer=tei__pb2.RerankStreamRequest.SerializeToString,
            response_deserializer=tei__pb2.RerankResponse.FromString,
            _registered_method=True)


class RerankServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Rerank(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RerankStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RerankServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Rerank': grpc.unary_unary_rpc_method_handler(
            servicer.Rerank,
            request_deserializer=tei__pb2.RerankRequest.FromString,
            response_serializer=tei__pb2.RerankResponse.SerializeToString,
        ),
        'RerankStream': grpc.stream_unary_rpc_method_handler(
            servicer.RerankStream,
            request_deserializer=tei__pb2.RerankStreamRequest.FromString,
            response_serializer=tei__pb2.RerankResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'tei.v1.Rerank', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('tei.v1.Rerank', rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Rerank(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Rerank(request,
               target,
               options=(),
               channel_credentials=None,
               call_credentials=None,
               insecure=False,
               compression=None,
               wait_for_ready=None,
               timeout=None,
               metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tei.v1.Rerank/Rerank',
            tei__pb2.RerankRequest.SerializeToString,
            tei__pb2.RerankResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RerankStream(request_iterator,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/tei.v1.Rerank/RerankStream',
            tei__pb2.RerankStreamRequest.SerializeToString,
            tei__pb2.RerankResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class TokenizeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Tokenize = channel.unary_unary(
            '/tei.v1.Tokenize/Tokenize',
            request_serializer=tei__pb2.EncodeRequest.SerializeToString,
            response_deserializer=tei__pb2.EncodeResponse.FromString,
            _registered_method=True)
        self.TokenizeStream = channel.stream_stream(
            '/tei.v1.Tokenize/TokenizeStream',
            request_serializer=tei__pb2.EncodeRequest.SerializeToString,
            response_deserializer=tei__pb2.EncodeResponse.FromString,
            _registered_method=True)
        self.Decode = channel.unary_unary(
            '/tei.v1.Tokenize/Decode',
            request_serializer=tei__pb2.DecodeRequest.SerializeToString,
            response_deserializer=tei__pb2.DecodeResponse.FromString,
            _registered_method=True)
        self.DecodeStream = channel.stream_stream(
            '/tei.v1.Tokenize/DecodeStream',
            request_serializer=tei__pb2.DecodeRequest.SerializeToString,
            response_deserializer=tei__pb2.DecodeResponse.FromString,
            _registered_method=True)


class TokenizeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Tokenize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenizeStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Decode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DecodeStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TokenizeServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Tokenize': grpc.unary_unary_rpc_method_handler(
            servicer.Tokenize,
            request_deserializer=tei__pb2.EncodeRequest.FromString,
            response_serializer=tei__pb2.EncodeResponse.SerializeToString,
        ),
        'TokenizeStream': grpc.stream_stream_rpc_method_handler(
            servicer.TokenizeStream,
            request_deserializer=tei__pb2.EncodeRequest.FromString,
            response_serializer=tei__pb2.EncodeResponse.SerializeToString,
        ),
        'Decode': grpc.unary_unary_rpc_method_handler(
            servicer.Decode,
            request_deserializer=tei__pb2.DecodeRequest.FromString,
            response_serializer=tei__pb2.DecodeResponse.SerializeToString,
        ),
        'DecodeStream': grpc.stream_stream_rpc_method_handler(
            servicer.DecodeStream,
            request_deserializer=tei__pb2.DecodeRequest.FromString,
            response_serializer=tei__pb2.DecodeResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'tei.v1.Tokenize', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('tei.v1.Tokenize', rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Tokenize(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Tokenize(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tei.v1.Tokenize/Tokenize',
            tei__pb2.EncodeRequest.SerializeToString,
            tei__pb2.EncodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def TokenizeStream(request_iterator,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/tei.v1.Tokenize/TokenizeStream',
            tei__pb2.EncodeRequest.SerializeToString,
            tei__pb2.EncodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Decode(request,
               target,
               options=(),
               channel_credentials=None,
               call_credentials=None,
               insecure=False,
               compression=None,
               wait_for_ready=None,
               timeout=None,
               metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/tei.v1.Tokenize/Decode',
            tei__pb2.DecodeRequest.SerializeToString,
            tei__pb2.DecodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DecodeStream(request_iterator,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/tei.v1.Tokenize/DecodeStream',
            tei__pb2.DecodeRequest.SerializeToString,
            tei__pb2.DecodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
