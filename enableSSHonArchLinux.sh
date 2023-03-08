pacman -Syu --noconfirm alsa-utils mpg123 openssh

systemctl enable sshd.service
systemctl start sshd.service

#amixer set Master 50%
