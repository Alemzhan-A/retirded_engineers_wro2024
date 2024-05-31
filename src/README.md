### Настройка Сетевого Взаимодействия между Raspberry Pi и EV3 с использованием ev3dev

Эта инструкция предназначена для установки и настройки сетевой связи между Raspberry Pi и EV3 для управления роботом. Raspberry Pi выступает в роли отправителя сигналов, а EV3 - в роли сервера, принимающего эти сигналы и корректирующего движение робота.

#### Подготовка и Установка

1. **Установка ОС и ПО**:
   - Скачайте и установите ev3dev с официального сайта на SD-карту для EV3.
   - Загрузите Raspberry Pi OS через Raspberry Pi Imager.
   - Установите и настройте приложения PuTTY и VNC Viewer для доступа к Raspberry Pi.

2. **Настройка Сети**:
   - Подключите Raspberry Pi и EV3 с помощью USB-MiniUSB кабеля.
   - Настройте статические IP адреса на обоих устройствах:
     - **Raspberry Pi**:
       ```bash
       sudo nano /etc/dhcpcd.conf
       # Добавьте следующие строки:
       interface wlan0
       static ip_address=192.168.42.3/24
       static routers=192.168.42.1
       static domain_name_servers=192.168.42.1 8.8.8.8
       ```
     - **EV3**:
       ```bash
       sudo nano /etc/network/interfaces
       # Добавьте следующие строки:
       auto usb0
       iface usb0 inet static
       address 192.168.42.3
       netmask 255.255.255.0
       sudo systemctl restart networking.service
       ```

3. **Автоматическая Настройка Сети при Запуске**:
   - Создайте скрипт на Raspberry Pi для автоматической настройки сети при подключении:
     ```bash
     sudo nano /usr/local/bin/setup_usb0.sh
     # Содержимое скрипта:
     #!/bin/bash
     # Wait for the USB device to become ready
     while ! ip link show usb0 | grep -q 'state UP'; do
         sleep 1
     done
     # Configure IP address
     sudo ip addr add 192.168.42.3/24 dev usb0
     sudo ip link set usb0 up
     sudo chmod +x /usr/local/bin/setup_usb0.sh
     ```
   - Зарегистрируйте этот скрипт в systemd для запуска при старте:
     ```bash
     sudo nano /etc/systemd/system/usb0-setup.service
     # Содержимое файла сервиса:
     [Unit]
     Description=Set up USB0 Network Interface at Boot
     Wants=network-online.target
     After=network-online.target

     [Service]
     Type=oneshot
     ExecStart=/usr/local/bin/setup_usb0.sh
     RemainAfterExit=yes

     [Install]
     WantedBy=multi-user.target
     sudo systemctl enable usb0-setup.service
     sudo systemctl start usb0-setup.service
     ```

4. **Перезагрузка Устройств**:
   - Выполните перезагрузку Raspberry Pi для проверки настроек: `sudo reboot`.

Теперь Raspberry Pi и EV3 будут автоматически готовы к работе после запуска, обеспечивая бесперебойное сетевое взаимодействие.
