# Redo the task #0 but by using Puppet
# install nginx & config int


exec { 'update package list':
  command => '/usr/bin/apt-get update',
  onlyif  => '/usr/bin/which nginx',
}

package { 'nginx':
  ensure => installed,
}

exec { 'create web directories':
  command => '/usr/bin/mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"',
}

exec { 'create index.html':
  command => '/usr/bin/echo "ALX SE" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
}

exec { 'remove current symlink':
  command => '/usr/bin/rm -rf /data/web_static/current',
}

exec { 'create new symlink':
  command => '/usr/bin/ln -s /data/web_static/releases/test/ /data/web_static/current',
}

exec { 'set ownership':
  command => '/usr/bin/chown -R ubuntu:ubuntu /data/',
}

exec { 'add location block config':
  command  => 'sudo sed -i "s|server_name _;|server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}|" /etc/nginx/sites-enabled/default',
  provider => shell,
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
