IMAGE=registry-nginx-proxy
TAG=0.1

OPT_DEPS=nginx.tar.gz
OPT_CLEAN=nginx.tar.gz

allovr: allovraux

include ../../../base/inc.mk

allovraux: all
	docker tag $(IMG_TAG) talou/$(IMAGE):$(TAG)

nginx.tar.gz: $(wildcard nginx/sites-available/*)
	tar czf $@ --owner=root --group=root -C nginx $(?:nginx/%=%)

