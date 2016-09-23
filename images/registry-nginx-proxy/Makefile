USER={{ user }}
IMAGE=registry-nginx-proxy
TAG=0.7

IMGTAG=$(USER)/$(IMAGE):$(TAG)
all: done

done: Dockerfile nginx.tar.gz
	docker build --no-cache . -t $(IMGTAG)
	@touch done

nginx.tar.gz: $(wildcard nginx/sites-available/*)
	tar czf $@ --owner=root --group=root -C nginx $(?:nginx/%=%)

push:
	docker push $(IMGTAG)

run:
	docker run -it $(IMGTAG) bash
	@echo

clean:
	rm -f done nginx.tar.gz
