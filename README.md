rpm-python-elasticsearch-curator
============

An RPM spec file build an RPM for [Elasticsearch Curator](https://github.com/elasticsearch/curator)

To Build:
```
sudo yum -y install rpmdevtools && rpmdev-setuptree

PKGNAME="python-elasticsearch-curator"
wget https://raw.github.com/mwhahaha/rpm-${PKGNAME}/master/${PKGNAME}.spec -O ~/rpmbuild/SPECS/${PKGNAME}.spec
spectool -R -g ~/rpmbuild/SPECS/${PKGNAME}.spec
rpmbuild -ba ~/rpmbuild/SPECS/${PKGNAME}.spec

```

### Source Attribution

Original source for spec from [Matt Dainty](https://gist.github.com/bodgit/57a3b562f08cc4916e7d) ([bodgit](https://github.com/bodgit)).
