# Linear tables

The tables of the workspace, with their columns. Assertions name a table as `entity` and its columns in `where`.

## `agent_sessions`

- `id`: varchar, primary key
- `commentId`: varchar, refers to `comments.id`

## `attachments`

- `id`: varchar, primary key
- `issueId`: varchar, refers to `issues.id`
- `originalIssueId`: varchar, refers to `issues.id`
- `archivedAt`: datetime
- `bodyData`: varchar
- `createdAt`: datetime
- `creatorId`: varchar, refers to `users.id`
- `externalUserCreatorId`: varchar, refers to `external_users.id`
- `groupBySource`: boolean
- `metadata`: jsonb
- `source`: jsonb
- `sourceType`: varchar
- `subtitle`: varchar
- `title`: varchar
- `updatedAt`: datetime
- `url`: varchar
- `iconUrl`: varchar

## `comment_subscribers_association`

- `comment_id`: varchar, primary key, refers to `comments.id`
- `user_id`: varchar, primary key, refers to `users.id`

## `comments`

- `id`: varchar, primary key
- `agentSessionId`: varchar, refers to `agent_sessions.id`
- `archivedAt`: datetime
- `body`: varchar
- `bodyData`: varchar
- `createdAt`: datetime
- `documentContentId`: varchar, refers to `document_contents.id`
- `documentId`: varchar, refers to `documents.id`
- `editedAt`: datetime
- `externalUserId`: varchar, refers to `external_users.id`
- `initiativeUpdateId`: varchar, refers to `initiative_updates.id`
- `issueId`: varchar, refers to `issues.id`
- `parentId`: varchar, refers to `comments.id`
- `postId`: varchar, refers to `posts.id`
- `projectId`: varchar, refers to `projects.id`
- `projectUpdateId`: varchar, refers to `project_updates.id`
- `quotedText`: varchar
- `reactionData`: jsonb
- `resolvedAt`: datetime
- `resolvingCommentId`: varchar, refers to `comments.id`
- `resolvingUserId`: varchar, refers to `users.id`
- `threadSummary`: jsonb
- `updatedAt`: datetime
- `url`: varchar
- `userId`: varchar, refers to `users.id`

## `customer_needs`

- `id`: varchar, primary key
- `originalIssueId`: varchar, refers to `issues.id`
- `issueId`: varchar, refers to `issues.id`
- `projectId`: varchar, refers to `projects.id`

## `cycles`

- `id`: varchar, primary key
- `archivedAt`: datetime
- `autoArchivedAt`: datetime
- `completedAt`: datetime
- `completedIssueCountHistory`: jsonb
- `completedScopeHistory`: jsonb
- `createdAt`: datetime
- `currentProgress`: jsonb
- `description`: varchar
- `endsAt`: datetime
- `inProgressScopeHistory`: jsonb
- `inheritedFromId`: varchar, refers to `cycles.id`
- `isActive`: boolean
- `isFuture`: boolean
- `isNext`: boolean
- `isPast`: boolean
- `isPrevious`: boolean
- `issueCountHistory`: jsonb
- `name`: varchar
- `number`: float
- `progress`: float
- `progressHistory`: jsonb
- `scopeHistory`: jsonb
- `startsAt`: datetime
- `teamId`: varchar, refers to `teams.id`
- `updatedAt`: datetime

## `document_contents`

- `id`: varchar, primary key
- `issueId`: varchar, refers to `issues.id`
- `projectId`: varchar, refers to `projects.id`
- `initiativeId`: varchar, refers to `initiatives.id`
- `archivedAt`: datetime
- `content`: varchar
- `contentState`: varchar
- `createdAt`: datetime
- `documentId`: varchar, refers to `documents.id`
- `projectMilestoneId`: varchar, refers to `project_milestones.id`
- `restoredAt`: datetime
- `updatedAt`: datetime

## `document_subscribers_association`

- `document_id`: varchar, primary key, refers to `documents.id`
- `user_id`: varchar, primary key, refers to `users.id`

## `documents`

- `id`: varchar, primary key
- `projectId`: varchar, refers to `projects.id`
- `archivedAt`: datetime
- `color`: varchar
- `content`: varchar
- `contentState`: varchar
- `createdAt`: datetime
- `creatorId`: varchar, refers to `users.id`
- `documentContentId`: varchar
- `hiddenAt`: datetime
- `icon`: varchar
- `initiativeId`: varchar, refers to `initiatives.id`
- `lastAppliedTemplateId`: varchar, refers to `templates.id`
- `resourceFolderId`: varchar
- `slugId`: varchar
- `sortOrder`: float
- `teamId`: varchar, refers to `teams.id`
- `title`: varchar
- `trashed`: boolean
- `updatedAt`: datetime
- `updatedById`: varchar, refers to `users.id`
- `url`: varchar

## `drafts`

- `id`: varchar, primary key
- `userId`: varchar, refers to `users.id`

## `entity_external_links`

- `id`: varchar, primary key
- `initiativeId`: varchar, refers to `initiatives.id`

## `external_users`

- `id`: varchar, primary key
- `archivedAt`: datetime
- `avatarUrl`: varchar
- `createdAt`: datetime
- `displayName`: varchar
- `email`: varchar
- `lastSeen`: datetime
- `name`: varchar
- `organizationId`: varchar, refers to `organizations.id`
- `updatedAt`: datetime

## `facets`

- `id`: varchar, primary key
- `sourceTeamId`: varchar, refers to `teams.id`
- `sourceOrganizationId`: varchar, refers to `organizations.id`
- `sourceProjectId`: varchar, refers to `projects.id`
- `sourceInitiativeId`: varchar, refers to `initiatives.id`

## `favorites`

- `id`: varchar, primary key
- `issueId`: varchar, refers to `issues.id`
- `projectId`: varchar, refers to `projects.id`

## `git_automation_states`

- `id`: varchar, primary key
- `teamId`: varchar, refers to `teams.id`

## `initiative_histories`

- `id`: varchar, primary key
- `initiativeId`: varchar, refers to `initiatives.id`

## `initiative_project_association`

- `initiative_id`: varchar, primary key, refers to `initiatives.id`
- `project_id`: varchar, primary key, refers to `projects.id`

## `initiative_relations`

- `id`: varchar, primary key
- `archivedAt`: datetime
- `createdAt`: datetime
- `sortOrder`: float
- `updatedAt`: datetime
- `initiativeId`: varchar, refers to `initiatives.id`
- `relatedInitiativeId`: varchar, refers to `initiatives.id`
- `userId`: varchar, refers to `users.id`

## `initiative_to_projects`

- `id`: varchar, primary key
- `archivedAt`: datetime
- `createdAt`: datetime
- `initiativeId`: varchar, refers to `initiatives.id`
- `projectId`: varchar, refers to `projects.id`
- `sortOrder`: varchar
- `updatedAt`: datetime

## `initiative_updates`

- `id`: varchar, primary key
- `initiativeId`: varchar, refers to `initiatives.id`

## `initiatives`

- `id`: varchar, primary key
- `archivedAt`: datetime
- `color`: varchar
- `completedAt`: datetime
- `content`: varchar
- `createdAt`: datetime
- `description`: varchar
- `creatorId`: varchar, refers to `users.id`
- `frequencyResolution`: varchar
- `health`: varchar
- `healthUpdatedAt`: datetime
- `icon`: varchar
- `lastUpdateId`: varchar, refers to `initiative_updates.id`
- `name`: varchar
- `organizationId`: varchar, refers to `organizations.id`
- `ownerId`: varchar, refers to `users.id`
- `parentInitiativeId`: varchar, refers to `initiatives.id`
- `slugId`: varchar
- `sortOrder`: float
- `startedAt`: datetime
- `status`: varchar
- `targetDate`: date
- `targetDateResolution`: varchar
- `trashed`: boolean
- `updateReminderFrequency`: float
- `updateReminderFrequencyInWeeks`: float
- `updateRemindersDay`: float
- `updateRemindersHour`: float
- `updatedAt`: datetime
- `url`: varchar

## `integrations`

- `id`: varchar, primary key
- `organizationId`: varchar, refers to `organizations.id`

## `integrations_settings`

- `id`: varchar, primary key
- `teamId`: varchar, refers to `teams.id`
- `projectId`: varchar, refers to `projects.id`
- `initiativeId`: varchar, refers to `initiatives.id`

## `issue_drafts`

- `id`: varchar, primary key
- `creatorId`: varchar, refers to `users.id`

## `issue_histories`

- `id`: varchar, primary key
- `issueId`: varchar, refers to `issues.id`
- `fromParentId`: varchar, refers to `issues.id`

## `issue_imports`

- `id`: varchar, primary key
- `archivedAt`: datetime
- `createdAt`: datetime
- `creatorId`: varchar, refers to `users.id`
- `csvFileUrl`: varchar
- `displayName`: varchar
- `error`: varchar
- `errorMetadata`: jsonb
- `mapping`: jsonb
- `progress`: float
- `service`: varchar
- `serviceMetadata`: jsonb
- `status`: varchar
- `teamName`: varchar
- `updatedAt`: datetime

## `issue_label_issue_association`

- `issue_id`: varchar, primary key, refers to `issues.id`
- `issue_label_id`: varchar, primary key, refers to `issue_labels.id`

## `issue_labels`

- `id`: varchar, primary key
- `teamId`: varchar, refers to `teams.id`
- `organizationId`: varchar, refers to `organizations.id`
- `archivedAt`: datetime
- `parentId`: varchar, refers to `issue_labels.id`
- `color`: varchar
- `createdAt`: datetime
- `creatorId`: varchar, refers to `users.id`
- `description`: varchar
- `inheritedFromId`: varchar, refers to `issue_labels.id`
- `isGroup`: boolean
- `lastAppliedAt`: datetime
- `name`: varchar
- `retiredAt`: datetime
- `updatedAt`: datetime

## `issue_relations`

- `id`: varchar, primary key
- `archivedAt`: datetime
- `createdAt`: datetime
- `issueId`: varchar, refers to `issues.id`
- `relatedIssueId`: varchar, refers to `issues.id`
- `type`: varchar
- `issueTitle`: varchar
- `relatedIssueTitle`: varchar
- `updatedAt`: datetime

## `issue_subscriber_user_association`

- `issue_id`: varchar, primary key, refers to `issues.id`
- `user_id`: varchar, primary key, refers to `users.id`

## `issue_suggestions`

- `id`: varchar, primary key
- `issueId`: varchar, refers to `issues.id`
- `suggestedIssueId`: varchar, refers to `issues.id`

## `issues`

- `id`: varchar, primary key
- `activitySummary`: jsonb
- `addedToCycleAt`: datetime
- `addedToProjectAt`: datetime
- `addedToTeamAt`: datetime
- `archivedAt`: datetime
- `asksExternalUserRequesterId`: varchar, refers to `external_users.id`
- `asksRequesterId`: varchar, refers to `users.id`
- `assigneeId`: varchar, refers to `users.id`
- `autoArchivedAt`: datetime
- `autoClosedAt`: datetime
- `autoClosedByParentClosing`: boolean
- `boardOrder`: float
- `branchName`: varchar
- `canceledAt`: datetime
- `parentId`: varchar, refers to `issues.id`
- `completedAt`: datetime
- `createdAt`: datetime
- `creatorId`: varchar, refers to `users.id`
- `customerTicketCount`: integer
- `cycleId`: varchar, refers to `cycles.id`
- `delegateId`: varchar, refers to `users.id`
- `description`: varchar
- `descriptionData`: jsonb
- `descriptionState`: varchar
- `dueDate`: date
- `estimate`: float
- `externalUserCreatorId`: varchar, refers to `external_users.id`
- `identifier`: varchar
- `integrationSourceType`: varchar
- `labelIds`: jsonb
- `lastAppliedTemplateId`: varchar, refers to `templates.id`
- `number`: float
- `previousIdentifiers`: jsonb
- `priority`: float
- `priorityLabel`: varchar
- `prioritySortOrder`: float
- `projectId`: varchar, refers to `projects.id`
- `projectMilestoneId`: varchar, refers to `project_milestones.id`
- `reactionData`: jsonb
- `slaBreachesAt`: datetime
- `slaHighRiskAt`: datetime
- `slaMediumRiskAt`: datetime
- `slaStartedAt`: datetime
- `slaType`: varchar
- `snoozedById`: varchar, refers to `users.id`
- `snoozedUntilAt`: datetime
- `sortOrder`: float
- `sourceCommentId`: varchar, refers to `comments.id`
- `startedAt`: datetime
- `startedTriageAt`: datetime
- `stateId`: varchar, refers to `workflow_states.id`
- `subIssueSortOrder`: float
- `suggestionsGeneratedAt`: datetime
- `teamId`: varchar, refers to `teams.id`
- `title`: varchar
- `trashed`: boolean
- `triagedAt`: datetime
- `updatedAt`: datetime
- `url`: varchar
- `uncompletedInCycleUponCloseId`: varchar, refers to `cycles.id`
- `reminderAt`: datetime

## `notifications`

- `id`: varchar, primary key
- `actorId`: varchar, refers to `users.id`
- `actorAvatarColor`: varchar
- `actorAvatarUrl`: varchar
- `actorInitials`: varchar
- `archivedAt`: datetime
- `category`: varchar
- `createdAt`: datetime
- `emailedAt`: datetime
- `externalUserActorId`: varchar, refers to `external_users.id`
- `groupingKey`: varchar
- `groupingPriority`: float
- `inboxUrl`: varchar
- `isLinearActor`: boolean
- `issueStatusType`: varchar
- `projectUpdateHealth`: varchar
- `readAt`: datetime
- `snoozedUntilAt`: datetime
- `subtitle`: varchar
- `title`: varchar
- `type`: varchar
- `unsnoozedAt`: datetime
- `updatedAt`: datetime
- `url`: varchar
- `userId`: varchar, refers to `users.id`
- `issueId`: varchar, refers to `issues.id`
- `initiativeId`: varchar, refers to `initiatives.id`
- `initiativeUpdateId`: varchar, refers to `initiative_updates.id`
- `projectId`: varchar, refers to `projects.id`
- `projectUpdateId`: varchar, refers to `project_updates.id`
- `oauthClientApprovalId`: varchar

## `organization_domains`

- `id`: varchar, primary key
- `archivedAt`: datetime
- `authType`: varchar
- `claimed`: boolean
- `createdAt`: datetime
- `creatorId`: varchar, refers to `users.id`
- `disableOrganizationCreation`: boolean
- `identityProviderId`: varchar
- `name`: varchar
- `updatedAt`: datetime
- `verificationEmail`: varchar
- `verified`: boolean

## `organization_invite_team`

- `organization_invite_id`: varchar, primary key, refers to `organization_invites.id`
- `team_id`: varchar, primary key, refers to `teams.id`

## `organization_invites`

- `id`: varchar, primary key
- `acceptedAt`: datetime
- `archivedAt`: datetime
- `createdAt`: datetime
- `email`: varchar
- `expiresAt`: datetime
- `external`: boolean
- `inviteeId`: varchar, refers to `users.id`
- `inviterId`: varchar, refers to `users.id`
- `metadata`: jsonb
- `organizationId`: varchar, refers to `organizations.id`
- `role`: varchar
- `updatedAt`: datetime

## `organizations`

- `id`: varchar, primary key
- `aiAddonEnabled`: boolean
- `aiTelemetryEnabled`: boolean
- `allowMembersToInvite`: boolean
- `allowedAuthServices`: jsonb
- `allowedFileUploadContentTypes`: jsonb
- `archivedAt`: datetime
- `createdAt`: datetime
- `createdIssueCount`: integer
- `customerCount`: integer
- `customersConfiguration`: jsonb
- `customersEnabled`: boolean
- `defaultFeedSummarySchedule`: varchar
- `deletionRequestedAt`: datetime
- `feedEnabled`: boolean
- `fiscalYearStartMonth`: float
- `gitBranchFormat`: varchar
- `gitLinkbackMessagesEnabled`: boolean
- `gitPublicLinkbackMessagesEnabled`: boolean
- `hipaaComplianceEnabled`: boolean
- `initiativeUpdateReminderFrequencyInWeeks`: float
- `initiativeUpdateRemindersDay`: varchar
- `initiativeUpdateRemindersHour`: float
- `logoUrl`: varchar
- `name`: varchar
- `oauthAppReview`: boolean
- `personalApiKeysEnabled`: boolean
- `periodUploadVolume`: float
- `previousUrlKeys`: jsonb
- `projectUpdateReminderFrequencyInWeeks`: float
- `projectUpdateRemindersDay`: varchar
- `projectUpdateRemindersHour`: float
- `projectUpdatesReminderFrequency`: varchar
- `reducedPersonalInformation`: boolean
- `releaseChannel`: varchar
- `restrictAgentInvocationToMembers`: boolean
- `restrictLabelManagementToAdmins`: boolean
- `restrictTeamCreationToAdmins`: boolean
- `roadmapEnabled`: boolean
- `samlEnabled`: boolean
- `samlSettings`: jsonb
- `scimEnabled`: boolean
- `scimSettings`: jsonb
- `slaDayCount`: varchar
- `slaEnabled`: boolean
- `themeSettings`: jsonb
- `trialEndsAt`: datetime
- `updatedAt`: datetime
- `urlKey`: varchar
- `userCount`: integer
- `workingDays`: jsonb

## `paid_subscriptions`

- `id`: varchar, primary key
- `organizationId`: varchar, refers to `organizations.id`

## `posts`

- `id`: varchar, primary key
- `teamId`: varchar, refers to `teams.id`
- `archivedAt`: datetime
- `audioSummary`: varchar
- `body`: varchar
- `bodyData`: varchar
- `createdAt`: datetime
- `creatorId`: varchar, refers to `users.id`
- `editedAt`: datetime
- `evalLogId`: varchar
- `feedSummaryScheduleAtCreate`: varchar
- `reactionData`: jsonb
- `slugId`: varchar
- `title`: varchar
- `ttlUrl`: varchar
- `type`: varchar
- `updatedAt`: datetime
- `userId`: varchar, refers to `users.id`
- `writtenSummaryData`: jsonb

## `project_histories`

- `id`: varchar, primary key
- `projectId`: varchar, refers to `projects.id`

## `project_label_project_association`

- `project_id`: varchar, primary key, refers to `projects.id`
- `project_label_id`: varchar, primary key, refers to `project_labels.id`

## `project_labels`

- `id`: varchar, primary key
- `organizationId`: varchar, refers to `organizations.id`
- `archivedAt`: datetime
- `parentId`: varchar, refers to `project_labels.id`
- `color`: varchar
- `createdAt`: datetime
- `creatorId`: varchar, refers to `users.id`
- `description`: varchar
- `isGroup`: boolean
- `lastAppliedAt`: datetime
- `name`: varchar
- `retiredAt`: datetime
- `updatedAt`: datetime

## `project_members_association`

- `project_id`: varchar, primary key, refers to `projects.id`
- `user_id`: varchar, primary key, refers to `users.id`

## `project_milestones`

- `id`: varchar, primary key
- `projectId`: varchar, refers to `projects.id`
- `archivedAt`: datetime
- `createdAt`: datetime
- `currentProgress`: jsonb
- `description`: varchar
- `descriptionData`: jsonb
- `descriptionState`: varchar
- `name`: varchar
- `progress`: float
- `progressHistory`: jsonb
- `sortOrder`: float
- `status`: varchar
- `targetDate`: date
- `updatedAt`: datetime

## `project_relations`

- `id`: varchar, primary key
- `projectId`: varchar, refers to `projects.id`
- `relatedProjectId`: varchar, refers to `projects.id`
- `anchorType`: varchar
- `archivedAt`: datetime
- `createdAt`: datetime
- `relatedAnchorType`: varchar
- `type`: varchar
- `updatedAt`: datetime
- `projectMilestoneId`: varchar, refers to `project_milestones.id`
- `relatedProjectMilestoneId`: varchar, refers to `project_milestones.id`
- `userId`: varchar, refers to `users.id`

## `project_statuses`

- `id`: varchar, primary key
- `organizationId`: varchar, refers to `organizations.id`
- `archivedAt`: datetime
- `color`: varchar
- `createdAt`: datetime
- `description`: varchar
- `indefinite`: boolean
- `name`: varchar
- `position`: float
- `type`: varchar
- `updatedAt`: datetime

## `project_updates`

- `id`: varchar, primary key
- `projectId`: varchar, refers to `projects.id`

## `projects`

- `id`: varchar, primary key
- `archivedAt`: datetime
- `autoArchivedAt`: datetime
- `canceledAt`: datetime
- `color`: varchar
- `completedAt`: datetime
- `completedIssueCountHistory`: jsonb
- `completedScopeHistory`: jsonb
- `content`: varchar
- `contentState`: varchar
- `convertedFromIssueId`: varchar, refers to `issues.id`
- `createdAt`: datetime
- `creatorId`: varchar, refers to `users.id`
- `currentProgress`: jsonb
- `description`: varchar
- `frequencyResolution`: varchar
- `health`: varchar
- `healthUpdatedAt`: datetime
- `icon`: varchar
- `inProgressScopeHistory`: jsonb
- `issueCountHistory`: jsonb
- `labelIds`: jsonb
- `lastAppliedTemplateId`: varchar, refers to `templates.id`
- `lastUpdateId`: varchar, refers to `project_updates.id`
- `leadId`: varchar, refers to `users.id`
- `name`: varchar
- `priority`: integer
- `priorityLabel`: varchar
- `prioritySortOrder`: float
- `progress`: float
- `progressHistory`: jsonb
- `projectUpdateRemindersPausedUntilAt`: datetime
- `scope`: float
- `scopeHistory`: jsonb
- `slackIssueComments`: boolean
- `slackIssueStatuses`: boolean
- `slackNewIssue`: boolean
- `slugId`: varchar
- `sortOrder`: float
- `startDate`: date
- `startDateResolution`: varchar
- `startedAt`: datetime
- `state`: varchar
- `statusId`: varchar, refers to `project_statuses.id`
- `targetDate`: date
- `targetDateResolution`: varchar
- `trashed`: boolean
- `updateReminderFrequency`: float
- `updateReminderFrequencyInWeeks`: float
- `updateRemindersDay`: float
- `updateRemindersHour`: float
- `updatedAt`: datetime
- `url`: varchar

## `reactions`

- `id`: varchar, primary key
- `issueId`: varchar, refers to `issues.id`
- `commentId`: varchar, refers to `comments.id`

## `team_memberships`

- `id`: varchar, primary key
- `userId`: varchar, refers to `users.id`
- `teamId`: varchar, refers to `teams.id`
- `archivedAt`: datetime
- `createdAt`: datetime
- `owner`: boolean
- `sortOrder`: float
- `updatedAt`: datetime

## `team_project_association`

- `team_id`: varchar, primary key, refers to `teams.id`
- `project_id`: varchar, primary key, refers to `projects.id`

## `teams`

- `id`: varchar, primary key
- `parentId`: varchar, refers to `teams.id`
- `activeCycleId`: varchar, refers to `cycles.id`
- `aiThreadSummariesEnabled`: boolean
- `archivedAt`: datetime
- `autoArchivePeriod`: float
- `autoCloseChildIssues`: boolean
- `autoCloseParentIssues`: boolean
- `autoClosePeriod`: float
- `autoCloseStateId`: varchar
- `color`: varchar
- `createdAt`: datetime
- `currentProgress`: jsonb
- `cycleCalenderUrl`: varchar
- `cycleCooldownTime`: float
- `cycleDuration`: float
- `cycleIssueAutoAssignCompleted`: boolean
- `cycleIssueAutoAssignStarted`: boolean
- `cycleLockToActive`: boolean
- `cycleStartDay`: float
- `cyclesEnabled`: boolean
- `defaultIssueEstimate`: float
- `defaultIssueStateId`: varchar, refers to `workflow_states.id`
- `defaultProjectTemplateId`: varchar, refers to `templates.id`
- `defaultTemplateForMembersId`: varchar, refers to `templates.id`
- `defaultTemplateForNonMembersId`: varchar, refers to `templates.id`
- `description`: varchar
- `displayName`: varchar
- `draftWorkflowStateId`: varchar, refers to `workflow_states.id`
- `groupIssueHistory`: boolean
- `icon`: varchar
- `inheritIssueEstimation`: boolean
- `inheritWorkflowStatuses`: boolean
- `inheritProductIntelligenceScope`: boolean
- `productIntelligenceScope`: varchar
- `inviteHash`: varchar
- `issueCount`: integer
- `issueEstimationAllowZero`: boolean
- `issueEstimationExtended`: boolean
- `issueEstimationType`: varchar
- `issueOrderingNoPriorityFirst`: boolean
- `issueSortOrderDefaultToBottom`: boolean
- `joinByDefault`: boolean
- `key`: varchar
- `markedAsDuplicateWorkflowStateId`: varchar, refers to `workflow_states.id`
- `mergeWorkflowStateId`: varchar, refers to `workflow_states.id`
- `mergeableWorkflowStateId`: varchar, refers to `workflow_states.id`
- `name`: varchar
- `organizationId`: varchar, refers to `organizations.id`
- `private`: boolean
- `progressHistory`: jsonb
- `requirePriorityToLeaveTriage`: boolean
- `reviewWorkflowStateId`: varchar, refers to `workflow_states.id`
- `scimGroupName`: varchar
- `scimManaged`: boolean
- `setIssueSortOrderOnStateChange`: varchar
- `slackIssueComments`: boolean
- `slackIssueStatuses`: boolean
- `slackNewIssue`: boolean
- `startWorkflowStateId`: varchar, refers to `workflow_states.id`
- `timezone`: varchar
- `triageEnabled`: boolean
- `triageIssueStateId`: varchar, refers to `workflow_states.id`
- `upcomingCycleCount`: float
- `updatedAt`: datetime

## `templates`

- `id`: varchar, primary key
- `teamId`: varchar, refers to `teams.id`
- `organizationId`: varchar, refers to `organizations.id`

## `triage_responsibilities`

- `id`: varchar, primary key
- `teamId`: varchar, refers to `teams.id`

## `user_flags`

- `id`: varchar, primary key
- `userId`: varchar, refers to `users.id`
- `flag`: varchar
- `value`: integer
- `lastSyncId`: float
- `createdAt`: datetime
- `updatedAt`: datetime

## `user_settings`

- `id`: varchar, primary key
- `userId`: varchar, refers to `users.id`
- `archivedAt`: datetime
- `autoAssignToSelf`: boolean
- `calendarHash`: varchar
- `createdAt`: datetime
- `notificationCategoryPreferences`: jsonb
- `notificationChannelPreferences`: jsonb
- `notificationDeliveryPreferences`: jsonb
- `showFullUserNames`: boolean
- `subscribedToChangelog`: boolean
- `subscribedToDPA`: boolean
- `subscribedToInviteAccepted`: boolean
- `subscribedToPrivacyLegalUpdates`: boolean
- `subscribedToGeneralMarketingCommunications`: boolean
- `unsubscribedFrom`: jsonb
- `updatedAt`: datetime
- `feedSummarySchedule`: varchar
- `settings`: jsonb
- `usageWarningHistory`: jsonb

## `users`

- `id`: varchar, primary key
- `active`: boolean
- `admin`: boolean
- `app`: boolean
- `archivedAt`: datetime
- `avatarBackgroundColor`: varchar
- `avatarUrl`: varchar
- `calendarHash`: varchar
- `canAccessAnyPublicTeam`: boolean
- `createdAt`: datetime
- `createdIssueCount`: integer
- `description`: varchar
- `disableReason`: varchar
- `displayName`: varchar
- `email`: varchar
- `gitHubUserId`: varchar
- `discordUserId`: varchar
- `guest`: boolean
- `initials`: varchar
- `inviteHash`: varchar
- `isAssignable`: boolean
- `isMe`: boolean
- `isMentionable`: boolean
- `lastSeen`: datetime
- `name`: varchar
- `organizationId`: varchar, refers to `organizations.id`
- `statusEmoji`: varchar
- `statusLabel`: varchar
- `statusUntilAt`: datetime
- `timezone`: varchar
- `updatedAt`: datetime
- `url`: varchar

## `webhooks`

- `id`: varchar, primary key
- `teamId`: varchar, refers to `teams.id`

## `workflow_states`

- `id`: varchar, primary key
- `teamId`: varchar, refers to `teams.id`
- `archivedAt`: datetime
- `color`: varchar
- `createdAt`: datetime
- `description`: varchar
- `inheritedFromId`: varchar, refers to `workflow_states.id`
- `name`: varchar
- `position`: float
- `type`: varchar
- `updatedAt`: datetime
