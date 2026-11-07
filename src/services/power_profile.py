from PySide6.QtCore import QObject, Slot, SLOT
from PySide6.QtDBus import QDBusConnection, QDBusInterface


SERVICE = "org.freedesktop.UPower.PowerProfiles"
PATH = "/org/freedesktop/UPower/PowerProfiles"
INTERFACE = "org.freedesktop.UPower.PowerProfiles"


class PowerProfileMonitor(QObject):

    def __init__(self, callback):
        super().__init__()

        self.callback = callback
        self.bus = QDBusConnection.systemBus()

        if not self.bus.isConnected():
            raise RuntimeError("Could not connect to system D-Bus")

        self.interface = QDBusInterface(
            SERVICE,
            PATH,
            INTERFACE,
            self.bus
        )

        if not self.interface.isValid():
            raise RuntimeError("Power Profiles D-Bus interface unavailable")

        # Subscribe to property changes
        connected = self.bus.connect(
            SERVICE,
            PATH,
            "org.freedesktop.DBus.Properties",
            "PropertiesChanged",
            self,
            SLOT(
                "handle_properties_changed(QString,QVariantMap,QStringList)"
            )
        )

        if not connected:
            raise RuntimeError("Could not subscribe to D-Bus signals")

        # Read the initial profile after subscribing
        current_profile = self.interface.property("ActiveProfile")

        if current_profile:
            self.callback(str(current_profile))

    @Slot(str, dict, "QStringList")
    def handle_properties_changed(
        self,
        interface_name,
        changed_properties,
        invalidated_properties
    ):

        if interface_name != INTERFACE:
            return

        profile = changed_properties.get("ActiveProfile")

        if profile is None:
            return

        # Unwrap D-Bus variant if necessary
        if hasattr(profile, "variant"):
            profile = profile.variant()

        self.callback(str(profile))