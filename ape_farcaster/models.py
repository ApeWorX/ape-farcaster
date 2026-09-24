from typing import Union

from humps import camelize
from pydantic import (
    BaseModel as PydanticBaseModel,
    ConfigDict,
    Field,
    PositiveInt,
    RootModel,
)


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(alias_generator=camelize, populate_by_name=True)


class ApiError(BaseModel):
    message: str


class ApiErrorResponse(BaseModel):
    errors: list[ApiError]


class ApiKeyStoreKey(BaseModel):
    key_id: str
    type: str
    base64_public_key: str
    base64_signature: str
    timestamp: PositiveInt
    fid: PositiveInt | None = None
    device_id: str | None = None
    device_name: str | None = None


class ApiToken(BaseModel):
    secret: str
    expires_at: PositiveInt


class ApiOpenGraphMetadata(BaseModel):
    url: str
    title: str | None = None
    description: str | None = None
    domain: str | None = None
    image: str | None = None
    logo: str | None = None
    use_large_image: bool | None = None
    stripped_cast_text: str | None = None


class ApiCastAttachments(BaseModel):
    open_graph: list[ApiOpenGraphMetadata] | None = None


class ApiOpenSeaNft(BaseModel):
    asset_contract_address: str
    token_id: str
    account_address: str


class ApiPfp(BaseModel):
    url: str
    verified: bool


class Bio(BaseModel):
    text: str
    mentions: list[str]


class ApiProfile(BaseModel):
    bio: Bio


class ViewerContext(BaseModel):
    following: bool | None = None
    followed_by: bool | None = None
    can_send_direct_casts: bool | None = None


class ApiUser(BaseModel):
    fid: PositiveInt
    username: str | None = None
    display_name: str | None = None
    registered_at: PositiveInt | None = None
    pfp: ApiPfp | None = None
    profile: ApiProfile
    follower_count: int
    following_count: int
    referrer_username: str | None = None
    viewer_context: ViewerContext | None = None


class ApiUserPreferences(BaseModel):
    send_email_on_mention: bool | None = None
    send_email_on_reply: bool | None = None
    send_email_on_reaction: bool | None = None
    send_email_on_follow: bool | None = None
    send_weekly_update_emails: bool | None = None
    send_product_update_emails: bool | None = None


class ApiAssetCollection(BaseModel):
    id: str
    name: str
    description: str | None = None
    item_count: int
    owner_count: int
    farcaster_owner_count: int
    image_url: str
    floor_price: str | None = None
    volume_traded: str
    external_url: str | None = None
    open_sea_url: str
    twitter_username: str | None = None
    schema_name: str | None = None


class LastSale(BaseModel):
    price: str
    date: str


class Mint(BaseModel):
    date: str
    transaction_hash: str


class ViewerContext1(BaseModel):
    liked: bool | None = None


class ApiAsset(BaseModel):
    id: str
    name: str
    contract_address: str
    token_id: str
    image_url: str
    external_url: str | None = None
    open_sea_url: str
    like_count: int
    uri: str
    collection: ApiAssetCollection
    owner: ApiUser | None = None
    last_sale: LastSale | None = None
    mint: Mint | None = None
    viewer_context: ViewerContext1 | None = None


class ApiAssetGroup(BaseModel):
    collection: ApiAssetCollection
    assets: list[ApiAsset]


class ApiAssetEvent(BaseModel):
    id: str
    timestamp: PositiveInt
    type: str
    verb: str
    asset: ApiAsset
    user: ApiUser


class ApiAssetEventFeedItem(BaseModel):
    id: str
    type: str
    latest_timestamp: PositiveInt
    events: list[ApiAssetEvent]


class ApiVerification(BaseModel):
    fid: PositiveInt
    address: str
    timestamp: PositiveInt


class ApiCastReaction(BaseModel):
    type: str
    hash: str
    reactor: ApiUser
    timestamp: PositiveInt
    cast_hash: str = Field(..., pattern=r"^0x[0-9a-fA-F]{40}$")


class ApiNewCollection(BaseModel):
    collection: ApiAssetCollection
    first_event: ApiAssetEvent


class ApiTopCollection(BaseModel):
    collection: ApiAssetCollection
    first_event: ApiAssetEvent


class ApiTrendingCollection(BaseModel):
    collection: ApiAssetCollection
    first_event: ApiAssetEvent
    recent_unique_users_count: int


class ApiRecaster(BaseModel):
    fid: PositiveInt
    username: str | None = None
    display_name: str | None = None


class Ancestors(BaseModel):
    count: int


class Replies(BaseModel):
    count: int


class Reactions(BaseModel):
    count: int


class Recasts(BaseModel):
    count: int
    recasters: list[ApiRecaster] | None = None


class Watches(BaseModel):
    count: int


class ViewerContext2(BaseModel):
    reacted: bool | None = None
    recast: bool | None = None
    watched: bool | None = None


class ParentSource(BaseModel):
    type: str
    url: str


class ApiCastUrlEmbed(BaseModel):
    type: str
    open_graph: ApiOpenGraphMetadata
    user: ApiUser | None = None
    asset: ApiAsset | None = None
    collection: ApiAssetCollection | None = None


class ApiCastImageEmbed(BaseModel):
    type: str
    url: str
    sourceUrl: str
    alt: str


class ApiCastUnknownEmbed(BaseModel):
    type: str
    source: str


class ApiCastEmbeds(BaseModel):
    images: list[ApiCastImageEmbed]
    urls: list[ApiCastUrlEmbed]
    unknowns: list[ApiCastUnknownEmbed]


class ApiCast(BaseModel):
    hash: str
    thread_hash: str | None = None
    parent_hash: str | None = None
    author: ApiUser
    parent_author: ApiUser | None = None
    parent_source: ParentSource | None = None
    text: str
    timestamp: PositiveInt
    mentions: list[ApiUser] | None = None
    attachments: ApiCastAttachments | None = None
    embeds: ApiCastEmbeds | None = None
    ancestors: Ancestors | None = None
    replies: Replies
    reactions: Reactions
    recasts: Recasts
    watches: Watches
    deleted: bool | None = None
    recast: bool | None = None
    viewer_context: ViewerContext2 | None = None


class ViewerContext3(BaseModel):
    sender: bool


class ApiDirectCast(BaseModel):
    sender: ApiUser
    text: str
    timestamp: PositiveInt
    viewer_context: ViewerContext3 | None = None


class ApiDirectCastConversation(BaseModel):
    conversation_id: str
    participants: list[ApiUser]
    last_direct_cast: ApiDirectCast
    timestamp: PositiveInt


class ApiUnseenConversation(BaseModel):
    conversation_id: str
    participant_fids: list[int]
    last_direct_cast_timestamp: PositiveInt


class ReactionContent(BaseModel):
    cast: ApiCast
    reaction: ApiCastReaction


class ApiNotificationCastReaction(BaseModel):
    type: str
    id: str
    timestamp: PositiveInt
    actor: ApiUser
    content: ReactionContent


class CastContent(BaseModel):
    cast: ApiCast


class ApiNotificationCastMention(BaseModel):
    type: str
    id: str
    timestamp: PositiveInt
    actor: ApiUser
    content: CastContent


class ApiNotificationCastReply(BaseModel):
    type: str
    id: str
    timestamp: PositiveInt
    actor: ApiUser
    content: CastContent


class ApiNotificationFollow(BaseModel):
    type: str
    id: str
    timestamp: PositiveInt
    actor: ApiUser


class RecastContent(BaseModel):
    recast: ApiCast
    recasted_cast: ApiCast


class ApiNotificationRecast(BaseModel):
    type: str
    id: str
    timestamp: PositiveInt
    actor: ApiUser
    content: RecastContent


class ReplyContent(BaseModel):
    cast: ApiCast
    reply: ApiCast


class ApiNotificationWatchedCastReply(BaseModel):
    type: str
    id: str
    timestamp: PositiveInt
    actor: ApiUser
    content: ReplyContent


class ApiNotification(
    RootModel[
        Union[
            ApiNotificationCastReaction,
            ApiNotificationCastMention,
            ApiNotificationCastReply,
            ApiNotificationFollow,
            ApiNotificationRecast,
            ApiNotificationWatchedCastReply,
        ]
    ]
):
    pass


class ApiCastReactionNotificationGroup(BaseModel):
    id: str
    type: str
    latest_timestamp: PositiveInt
    total_item_count: int
    preview_items: list[ApiNotificationCastReaction]


class ApiCastMentionNotificationGroup(BaseModel):
    id: str
    type: str
    latest_timestamp: PositiveInt
    total_item_count: int
    preview_items: list[ApiNotificationCastMention]


class ApiCastReplyNotificationGroup(BaseModel):
    id: str
    type: str
    latest_timestamp: PositiveInt
    total_item_count: int
    preview_items: list[ApiNotificationCastReply]


class ApiFollowNotificationGroup(BaseModel):
    id: str
    type: str
    latest_timestamp: PositiveInt
    total_item_count: int
    preview_items: list[ApiNotificationFollow]


class ApiRecastNotificationGroup(BaseModel):
    id: str
    type: str
    latest_timestamp: PositiveInt
    total_item_count: int
    preview_items: list[ApiNotificationRecast]


class ApiWatchedCastReplyNotificationGroup(BaseModel):
    id: str
    type: str
    latest_timestamp: PositiveInt
    total_item_count: int
    preview_items: list[ApiNotificationWatchedCastReply]


class ApiNotificationGroup(
    RootModel[
        Union[
            ApiCastReactionNotificationGroup,
            ApiCastMentionNotificationGroup,
            ApiCastReplyNotificationGroup,
            ApiFollowNotificationGroup,
            ApiRecastNotificationGroup,
            ApiWatchedCastReplyNotificationGroup,
        ]
    ]
):
    pass


class ApiCastFeedItem(BaseModel):
    id: str
    timestamp: PositiveInt
    cast: ApiCast
    replies: list[ApiCast] | None = None
    other_participants: list[ApiUser]


class ViewCastPushNotification(BaseModel):
    id: str
    type: str
    merkle_root: str
    thread_merkle_root: str
    cast_fid: float
    cast_hash: str


class UnreadDirectCastPushNotification(BaseModel):
    id: str
    type: str


class PushNotificationPayload(
    RootModel[Union[ViewCastPushNotification, UnreadDirectCastPushNotification]]
):
    pass


class Result(BaseModel):
    status: str


class HealthcheckGetResponse(BaseModel):
    result: Result


class Next(BaseModel):
    cursor: str | None = None


class EventsResult(BaseModel):
    events: list[ApiAssetEvent]


class IterableEventsResult(BaseModel):
    events: list[ApiAssetEvent]
    cursor: str | None = None


class AssetEventsGetResponse(BaseModel):
    result: EventsResult
    next: Next | None = None


class AssetResult(BaseModel):
    asset: ApiAsset


class AssetGetResponse(BaseModel):
    result: AssetResult


class AuthParams(BaseModel):
    timestamp: PositiveInt
    expires_at: PositiveInt


class AuthPutRequest(BaseModel):
    method: str = "generateToken"
    params: AuthParams


class TokenResult(BaseModel):
    token: ApiToken


class AuthPutResponse(BaseModel):
    result: TokenResult


class Timestamp(BaseModel):
    timestamp: PositiveInt


class AuthDeleteRequest(BaseModel):
    method: str = "revokeToken"
    params: Timestamp


class AssetsResult(BaseModel):
    assets: list[ApiAsset]


class CastsResult(BaseModel):
    casts: list[ApiCast]


class IterableCastsResult(BaseModel):
    casts: list[ApiCast]
    cursor: str | None = None


class CastsGetResponse(BaseModel):
    result: CastsResult
    next: Next | None = None


class Parent(BaseModel):
    fid: PositiveInt
    hash: str


class CastsPostRequest(BaseModel):
    text: str
    embeds: list[str] | None = None
    parent: Parent | None = None
    channel_key: str | None = None


class CastsPostResponse(BaseModel):
    result: CastContent


class CastGetResponse(BaseModel):
    result: CastContent


class CastHash(BaseModel):
    cast_hash: str


class ReactionsResult(BaseModel):
    likes: list[ApiCastReaction]


class IterableReactionsResult(BaseModel):
    likes: list[ApiCastReaction]
    cursor: str | None = None


class ReactionsPutResult(BaseModel):
    like: ApiCastReaction


class CastReactionsGetResponse(BaseModel):
    result: ReactionsResult
    next: Next | None = None


class CastReactionsPutRequest(BaseModel):
    type: str
    cast_fid: PositiveInt
    cast_hash: str


class CastReactionsPutResponse(BaseModel):
    result: ReactionsPutResult


class CastReactionsDeleteRequest(BaseModel):
    type: str
    cast_fid: PositiveInt
    cast_hash: str


class UsersResult(BaseModel):
    users: list[ApiUser]


class IterableUsersResult(BaseModel):
    users: list[ApiUser]
    cursor: str | None = None


class CastRecastersGetResponse(BaseModel):
    result: UsersResult
    next: Next | None = None


class CollectionsResult(BaseModel):
    collections: list[ApiAssetCollection]


class IterableCollectionsResult(BaseModel):
    collections: list[ApiAssetCollection]
    cursor: str | None = None


class UserCollectionsGetResponse(BaseModel):
    result: CollectionsResult
    next: Next | None = None


class CollectionOwnersGetResponse(BaseModel):
    result: UsersResult
    next: Next | None = None


class FollowsPutRequest(BaseModel):
    target_fid: PositiveInt


class StatusContent(BaseModel):
    success: bool


class StatusResponse(BaseModel):
    result: StatusContent


class FollowsDeleteRequest(BaseModel):
    target_fid: PositiveInt


class CustodyAddress(BaseModel):
    custody_address: str = Field(..., pattern=r"^0[xX][0-9a-fA-F]{40}$")


class CustodyAddressGetResponse(BaseModel):
    result: CustodyAddress


class Likes(BaseModel):
    likes: list[ApiCastReaction]


class IterableLikes(BaseModel):
    likes: list[ApiCastReaction]
    cursor: str | None = None


class UserCastLikesGetResponse(BaseModel):
    result: Likes
    next: Next | None = None


class FollowersGetResponse(BaseModel):
    result: UsersResult
    next: Next | None = None


class FollowingGetResponse(BaseModel):
    result: UsersResult
    next: Next | None = None


class UsersGetResponse(BaseModel):
    result: UsersResult
    next: Next | None = None


class UserResult(BaseModel):
    user: ApiUser


class MeGetResponse(BaseModel):
    result: UserResult


class MentionNotification(BaseModel):
    type: str = "cast-mention"
    id: str
    timestamp: PositiveInt
    actor: ApiUser
    content: CastContent


class ReplyNotification(BaseModel):
    type: str = "cast-reply"
    id: str
    timestamp: PositiveInt
    actor: ApiUser
    content: CastContent


class NotificationsResult(BaseModel):
    notifications: list[MentionNotification | ReplyNotification]


class IterableNotificationsResult(BaseModel):
    notifications: list[MentionNotification | ReplyNotification]
    cursor: str | None = None


class MentionAndReplyNotificationsGetResponse(BaseModel):
    result: NotificationsResult
    next: Next | None = None


class RecastsPutResponse(BaseModel):
    result: CastHash


class UserGetResponse(BaseModel):
    result: UserResult


class UserByUsernameGetResponse(BaseModel):
    result: UserResult


class VerificationsResult(BaseModel):
    verifications: list[ApiVerification]


class IterableVerificationsResult(BaseModel):
    verifications: list[ApiVerification]
    cursor: str | None = None


class VerificationsGetResponse(BaseModel):
    result: VerificationsResult
    next: Next | None = None


class CastLikesPutResponse(BaseModel):
    result: ReactionsResult


class CastLikesGetResponse(BaseModel):
    result: ReactionsResult
    next: Next | None = None
