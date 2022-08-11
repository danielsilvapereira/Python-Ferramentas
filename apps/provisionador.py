import PySimpleGUI as sg


class TelaPython:
    def _init_(self):
        sg.theme('BrownBlue')
        # Layout
        layout = [
            [sg.Text('Nome', size=(10, 0), justification='center'), sg.Input(key='nome')],
            [sg.Text('N da Casa', size=(10, 0), justification='center'), sg.Input(key='casa')],
            [sg.Text('Serial', size=(10, 0), justification='center'), sg.Input(key='serial')],
            [sg.Text('Porta', size=(10, 0), justification='center'), sg.Input(key='porta')],
            [sg.Text('ID', size=(10, 0), justification='center'), sg.Input(key='id')],
            [sg.Text('VLAN', size=(10, 0), justification='center'), sg.Input(key='vlan')],
            [sg.Button('Gerar')],
            [sg.Output(size=(130, 27), key='output')]
        ]
        # Janela
        self.janela = sg.Window("GERADOR DE SCRIPT").layout(layout)

    def Iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values = self.janela.Read()
            self.janela.FindElement('output').Update('')
            nome = self.values['nome']
            casa = self.values['casa']
            serial = self.values['serial']
            porta = self.values['porta']
            id = self.values['id']
            vlan = self.values['vlan']
            print(f"""
conf t
interface gpon_olt-1/3/{porta}
onu {id} type F612W sn {serial}
exit
!
interface gpon_onu-1/3/{porta}:{id}
name 2{casa} {nome} - CONDOMINIO JARDIM DO SOL
sn-bind enable sn
tcont 4 profile SMARTOLT-1G-UP
gemport 1 tcont 4
exit
interface vport-1/3/{porta}.{id}:1
service-port 1 user-vlan {vlan} vlan {vlan}
!
pon-onu-mng gpon_onu-1/3/{porta}:{id}
wan 1 ethuni 1 service voip
service 1 gemport 1 vlan {vlan}
security-mgmt 1 state enable mode forward ingress-type wan protocol web
interface eth eth_0/1 state lock
interface eth eth_0/2 state lock
voip protocol sip
voip-ip ipv4 mode dhcp vlan-profile VOIP host 2
sip-service pots_0/1 profile VOIP_COND.J_SOL userid 2{casa} username 2{casa} password J@rdim@2{casa}
exit
exit
write""")


tela = TelaPython()
tela.Iniciar()
