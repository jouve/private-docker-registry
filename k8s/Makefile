TPLS=$(wildcard tpl/*)
BTPLS=$(TPLS:tpl/%=%)
TGT=$(BTPLS:%.j2=%)
NAMESPACE?=default

all: $(TGT)

%.yaml: tpl/%.yaml.j2
	sh -c "echo \"namespace: $(NAMESPACE)\" | jinjagen.py -d - -o $@ $<"

clean:
	rm -f $(TGT)

