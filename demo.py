#!/usr/bin/env python3

import kreate

app = kreate.App('demo', 'acc', 'v1.2')
app.labels["egress-to-oracle"] = "enabled"

kust = kreate.Kustomization(app)

ingr = kust.add(kreate.Ingress(app, sticky=True))
ingr.whitelist("ggg")
ingr.basic_auth()

depl = kust.add(kreate.Deployment(app))

kust.kreate()
