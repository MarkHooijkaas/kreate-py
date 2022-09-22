#!/usr/bin/env python3

import kreate

app = kreate.App('demo', 'v1.2')
app.labels["egress-to-oracle"] = "enabled"

env = kreate.Environment(app, 'acc')
env.project = "kreate-test"

kust = kreate.Kustomization(env)

ingr = kust.add(kreate.Ingress(env, sticky=True))
ingr.whitelist("ggg")
ingr.basic_auth()

depl = kust.add(kreate.Deployment(env))

kust.kreate()
