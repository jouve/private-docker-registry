private docker registry
=======================

* `bin/docker-catalog.py` allow to query docker registry:2
* `images/registry-nginx-proxy` is a nginx proxy to trick docker registry into thinking it's talking on localhost
* `k8s/registry` contains some kubernetes yaml files, 2 vars should be replaced :
	* `{{ namespace }}` is the namespace to use
	* `{{ registry_nginx_proxy_image }}` the registry-nginx-proxy image

