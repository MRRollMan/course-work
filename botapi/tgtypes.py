import typing
from dataclasses import dataclass, field

if typing.TYPE_CHECKING:
    from api import API


@dataclass
class User:
    id: typing.Optional[int] = None
    is_bot: typing.Optional[bool] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    username: typing.Optional[str] = None
    language_code: typing.Optional[str] = None
    is_premium: typing.Optional[bool] = False
    added_to_attachment_menu: typing.Optional[bool] = False
    can_join_groups: typing.Optional[bool] = None
    can_read_all_group_messages: typing.Optional[bool] = None
    supports_inline_queries: typing.Optional[bool] = None


@dataclass
class Update:
    update_id: int
    message: typing.Optional["Message"] = None

    API: typing.Optional["API"] = None
    payload: dict = field(default_factory=dict)

    def __post_init__(self):
        if isinstance(self.message, dict):
            self.message = Message.from_telegram(self.message)


@dataclass
class Message:
    from_user: typing.Optional["User"] = field(metadata={"name": "from"})
    message_id: typing.Optional[int] = None
    sender_chat: typing.Optional["Chat"] = None
    date: typing.Optional[int] = None
    chat: typing.Optional["Chat"] = None
    forward_from: typing.Optional["User"] = None
    forward_from_chat: typing.Optional["Chat"] = None
    forward_from_message_id: typing.Optional[int] = None
    forward_signature: typing.Optional[str] = None
    forward_sender_name: typing.Optional[str] = None
    forward_date: typing.Optional[int] = None
    is_automatic_forward: typing.Optional[bool] = None
    reply_to_message: typing.Optional["Message"] = None
    via_bot: typing.Optional["User"] = None
    edit_date: typing.Optional[int] = None
    has_protected_content: typing.Optional[bool] = None
    media_group_id: typing.Optional[str] = None
    author_signature: typing.Optional[str] = None
    text: typing.Optional[str] = None
    entities: typing.Optional[typing.List[dict]] = None
    animation: typing.Optional[dict] = None
    audio: typing.Optional[dict] = None
    document: typing.Optional[dict] = None
    photo: typing.Optional[typing.List[dict]] = None
    sticker: typing.Optional[dict] = None
    video: typing.Optional[dict] = None
    video_note: typing.Optional[dict] = None
    voice: typing.Optional[dict] = None
    caption: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List[dict]] = None
    contact: typing.Optional[dict] = None
    dice: typing.Optional[dict] = None
    game: typing.Optional[dict] = None
    poll: typing.Optional[dict] = None
    venue: typing.Optional[dict] = None
    location: typing.Optional[dict] = None
    new_chat_members: typing.Optional[typing.List[typing.Optional[dict]]] = None
    left_chat_member: typing.Optional["User"] = None
    new_chat_title: typing.Optional[str] = None
    new_chat_photo: typing.Optional[typing.List[dict]] = None
    delete_chat_photo: typing.Optional[bool] = None
    group_chat_created: typing.Optional[bool] = None
    supergroup_chat_created: typing.Optional[bool] = None
    channel_chat_created: typing.Optional[bool] = None
    message_auto_delete_timer_changed: typing.Optional[dict] = None
    migrate_to_chat_id: typing.Optional[int] = None
    migrate_from_chat_id: typing.Optional[int] = None
    pinned_message: typing.Optional[dict] = None
    invoice: typing.Optional[dict] = None
    successful_payment: typing.Optional[dict] = None
    connected_website: typing.Optional[str] = None
    passport_data: typing.Optional[dict] = None
    proximity_alert_triggered: typing.Optional[dict] = None
    video_chat_scheduled: typing.Optional[dict] = None
    video_chat_started: typing.Optional[dict] = None
    video_chat_ended: typing.Optional[dict] = None
    video_chat_participants_invited: typing.Optional[dict] = None
    web_app_data: typing.Optional[dict] = None
    reply_markup: typing.Optional[dict] = None

    def __post_init__(self):
        if isinstance(self.from_user, dict):
            self.from_user = User(**self.from_user)
        if isinstance(self.forward_from, dict):
            self.forward_from = User(**self.forward_from)
        if isinstance(self.via_bot, dict):
            self.via_bot = User(**self.via_bot)
        if isinstance(self.left_chat_member, dict):
            self.left_chat_member = User(**self.left_chat_member)
        if isinstance(self.sender_chat, dict):
            self.sender_chat = Chat(**self.sender_chat)
        if isinstance(self.chat, dict):
            self.chat = Chat(**self.chat)
        if isinstance(self.forward_from_chat, dict):
            self.forward_from_chat = Chat(**self.forward_from_chat)

    @staticmethod
    def from_telegram(d: dict):
        d["from_user"] = d.pop("from")
        return Message(**d)


@dataclass
class Chat:
    id: typing.Optional[int] = None
    type: typing.Optional[str] = None
    title: typing.Optional[str] = None
    username: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    photo: typing.Optional[dict] = None
    bio: typing.Optional[str] = None
    has_private_forwards: typing.Optional[bool] = None
    description: typing.Optional[str] = None
    invite_link: typing.Optional[str] = None
    pinned_message: typing.Optional["Message"] = None
    permissions: typing.Optional[dict] = None
    slow_mode_delay: typing.Optional[int] = None
    message_auto_delete_time: typing.Optional[int] = None
    has_protected_content: typing.Optional[bool] = None
    sticker_set_name: typing.Optional[str] = None
    can_set_sticker_set: typing.Optional[bool] = None
    linked_chat_id: typing.Optional[int] = None
    location: typing.Optional[dict] = None

    def __post_init__(self):
        if isinstance(self.pinned_message, dict):
            self.pinned_message = Message(**self.pinned_message)
