#!/usr/bin/env python

import transmissionrpc

tc = transmissionrpc.Client('localhost', port=9091)
torrents = tc.get_torrents()

for torrent in torrents:
    if torrent.status == 'seeding':
        torrent.stop()
        tc.remove_torrent(torrent.id)
    elif torrent.status == 'stopped':
        tc.remove_torrent(torrent.id)
