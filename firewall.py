from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

BLOCKED_MAC = "REPLACE_WITH_H2_MAC"

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet:
        return

    src = str(packet.src)
    dst = str(packet.dst)

    log.info("Packet: %s -> %s", src, dst)

    if src == BLOCKED_MAC:
        log.info("🚫 BLOCKED HOST: %s", src)

        msg = of.ofp_flow_mod()
        msg.match.dl_src = packet.src
        msg.priority = 100
        event.connection.send(msg)
        return

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
