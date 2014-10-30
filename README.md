rpm-elasticsearch-curator
============

An RPM spec file build an RPM for [Elasticsearch Curator](http://github.com/elasticsearch/curator)

To Build:
```
sudo yum -y install rpmdevtools && rpmdev-setuptree

PKGNAME="python-elasticsearch-curator"
wget https://raw.github.com/mwhahaha/rpm-${PKGNAME}/master/${PKGNAME}.spec -O ~/rpmbuild/SPECS/${PKGNAME}.spec`
spectool -R -n -g ~/rpmbuild/SPECS/${PKGNAME}.spec
rpmbuild -ba ~/rpmbuild/SPECS/${PKGNAME}.spec

```

### Source Attribution

Original source for spec from [Matt Dainty <matt@bodgit-n-scarper.com> (bodgit)](https://gist.github.com/bodgit/57a3b562f08cc4916e7d).
