from orca.common.clients import k8s


class ResourceProxyFactory(object):

    @staticmethod
    def get(k8s_client, kind):
        if kind == 'virtual_service':
            return k8s.CustomResourceProxy(
                k8s_client.CustomObjectsApi().list_cluster_custom_object,
                group="networking.istio.io",
                version="v1alpha3",
                plural="virtualservices")
        else:
            raise Exception("Unknown kind %s" % kind)
