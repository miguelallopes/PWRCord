class DefaultMessageNotificationLevel:
    ALL_MESSAGES: int = 0
    """members will receive notifications for all messages by default"""
    ONLY_MENTIONS: int = 1
    """members will receive notifications only for messages that @mention them by default"""


class ExplicitContentFilterLevel:
    DISABLED: int = 0
    """media content will not be scanned"""
    MEMBERS_WITHOUT_ROLES: int = 1
    """media content sent by members without roles will be scanned"""
    ALL_MEMBERS: int = 2
    """media content sent by all members will be scanned"""


class MFALevel:
    NONE: int = 0
    """guild has no MFA/2FA requirement for moderation actions"""

    ELEVATED: int = 1
    """guild has a 2FA requirement for moderation actions"""


class VerificationLevel:
    NONE: int = 0
    """unrestricted"""
    LOW: int = 1
    """must have verified email on account"""
    MEDIUM: int = 2
    """must be registered on Discord for longer than 5 minutes"""
    HIGH: int = 3
    """must be a member of the server for longer than 10 minutes"""
    VERY_HIGH: int = 4
    """must have a verified phone number"""


class PremiumTier:
    NONE: int = 0
    """guild has not unlocked any Server Boost perks"""
    TIER_1: int = 1
    """guild has unlocked Server Boost level 1 perks"""
    TIER_2: int = 2
    """guild has unlocked Server Boost level 2 perks"""
    TIER_3: int = 3
    """guild has unlocked Server Boost level 3 perks"""


class SystemChannelFlags:
    SUPPRESS_JOIN_NOTIFICATIONS: int = 1 << 0
    """Suppress member join notifications"""
    SUPPRESS_PREMIUM_NOTIFICATIONS: int = 1 << 1
    """Suppress server boost notifications"""
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS: int = 1 << 2
    """Suppress server setup tips"""
    SUPPRESS_JOIN_NOTIFICATIONS_REPLIES: int = 1 << 3
    """Hide member join sticker reply buttons"""


class GuildFeature:
    ANIMATED_ICON: str = "ANIMATED_ICON"
    """guild has access to set an animated guild icon"""
    BANNER: str = "BANNER"
    """guild has access to set a guild banner image"""
    COMMERCE: str = "COMMERCE"
    """guild has access to use commerce features (i.e. create store channels)"""
    COMMUNITY: str = "COMMUNITY"
    """guild can enable welcome screen, Membership Screening, stage channels and discovery, and receives community updates"""
    DISCOVERABLE: str = "DISCOVERABLE"
    """guild is able to be discovered in the directory"""
    FEATURABLE: str = "FEATURABLE"
    """guild is able to be featured in the directory"""
    INVITE_SPLASH: str = "INVITE_SPLASH"
    """guild has access to set an invite splash background"""
    MEMBER_VERIFICATION_GATE_ENABLED: str = "MEMBER_VERIFICATION_GATE_ENABLED"
    """guild has enabled Membership Screening"""
    MONETIZATION_ENABLED: str = "MONETIZATION_ENABLED"
    """guild has enabled monetization"""
    MORE_STICKERS: str = "MORE_STICKERS"
    """guild has increased custom sticker slots"""
    NEWS: str = "NEWS"
    """guild has access to create news channels"""
    PARTNERED: str = "PARTNERED"
    """guild is partnered"""
    PREVIEW_ENABLED: str = "PREVIEW_ENABLED"
    """guild can be previewed before joining via Membership Screening or the directory"""
    PRIVATE_THREADS: str = "PRIVATE_THREADS"
    """guild has access to create private threads"""
    ROLE_ICONS: str = "ROLE_ICONS"
    """guild is able to set role icons"""
    SEVEN_DAY_THREAD_ARCHIVE: str = "SEVEN_DAY_THREAD_ARCHIVE"
    """guild has access to the seven day archive time for threads"""
    THREE_DAY_THREAD_ARCHIVE: str = "THREE_DAY_THREAD_ARCHIVE"
    """guild has access to the three day archive time for threads"""
    TICKETED_EVENTS_ENABLED: str = "TICKETED_EVENTS_ENABLED"
    """guild has enabled ticketed events"""
    VANITY_URL: str = "VANITY_URL"
    """guild has access to set a vanity URL"""
    VERIFIED: str = "VERIFIED"
    """guild is verified"""
    VIP_REGIONS: str = "VIP_REGIONS"
    """guild has access to set 384kbps bitrate in voice (previously VIP voice servers)"""
    WELCOME_SCREEN_ENABLED: str = "WELCOME_SCREEN_ENABLED"
    """guild has enabled the welcome screen"""
