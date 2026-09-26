# Code Orange Dev School - PR Tracking Dashboard

> **Tracking every pull request by Code Orange community members to Bitcoin open-source projects.**
>
> Last updated: 26 September 2026 (full re-verification with `tools/verify_dashboard.py`) | Checked weekly by CI

---

## Summary

| Metric | Count |
| --- | --- |
| **PRs Merged (direct link for every one)** | **131** |
| **PRs Open / Under Review** | **24** |
| **Total PRs Opened** | **155+** (merged + open; closed-unmerged not counted) |
| **Distinct Projects Contributed To** | **30+** |
| **Active Contributors (linked below)** | **12** |
| **Emerging Contributors (first PR imminent)** | **4** |

Highlights: **3 merged Bitcoin Core** PRs (Peter ×2, Muhammad), **9 merged rust-payjoin** PRs across three contributors (Vaan ×5, Arowolo ×3, Mwihoti ×1), merged PRs in **rust-bitcoin** (Peter ×2, Vaan, Muhammad, Gradale), **hex-conservative**, **Floresta**, **BDK/bdk-cli/bdk_wallet/bdk-ffi**, **LDK**, and **peer-observer** ×4.

---

## Current Metrics Data Contract

This dashboard is Code Orange's public source for **current PR output**. Historical reports and contributor profiles may use earlier snapshots and must link here rather than repeat these totals.

| Field | Rule |
| --- | --- |
| **Reporting cutoff** | Full link-level verification through **26 September 2026**. |
| **Attribution** | Count only in-scope Bitcoin OSS PRs with a direct link. PRs made before a developer joined Code Orange may be listed as history, but are excluded from program-outcome claims. |
| **PR state** | *Merged* means accepted upstream. *Open / under review* means submitted and neither merged nor closed at the reporting cutoff. Closed-unmerged PRs are not counted as open. |
| **Active contributor** | A unique named community member with an in-scope PR that is open/under review or had a verified merged contribution in the reporting window. Re-verify the label at each monthly update. |
| **Metric owner** | The named Code Orange **PR Verifier**, recorded in the weekly operating scorecard. |
| **Cadence** | Verify state changes weekly; publish this dashboard's refreshed public snapshot monthly, with the cutoff date shown. |

**Counting note:** the 96 merged total is the sum of the linked developer rows below. The table also contains one prospective contributor whose GitHub handle is pending; that person is not included in the four verified emerging contributors.

---

## Merged Pull Requests by Developer (131)

### Peter ([@pzafonte](https://github.com/pzafonte)) - 30 merged
| Project | PR | Date |
| --- | --- | --- |
| **Bitcoin Core** | [bitcoin/bitcoin #34885](https://github.com/bitcoin/bitcoin/pull/34885) | Apr 2026 |
| **Bitcoin Core** | [bitcoin/bitcoin #35380](https://github.com/bitcoin/bitcoin/pull/35380) - kernel: expose witness/scriptSig (Silent Payments scanning) | Jul 2026 |
| rust-bitcoin | [#5968](https://github.com/rust-bitcoin/rust-bitcoin/pull/5968) | Apr 2026 |
| rust-bitcoin | [#5917](https://github.com/rust-bitcoin/rust-bitcoin/pull/5917) | Apr 2026 |
| kernel-node | [#105](https://github.com/kernel-node/kernel-node/pull/105) · [#104](https://github.com/kernel-node/kernel-node/pull/104) · [#103](https://github.com/kernel-node/kernel-node/pull/103) · [#99](https://github.com/kernel-node/kernel-node/pull/99) · [#95](https://github.com/kernel-node/kernel-node/pull/95) · [#94](https://github.com/kernel-node/kernel-node/pull/94) · [#93](https://github.com/kernel-node/kernel-node/pull/93) · [#90](https://github.com/kernel-node/kernel-node/pull/90) · [#88](https://github.com/kernel-node/kernel-node/pull/88) · [#87](https://github.com/kernel-node/kernel-node/pull/87) · [#86](https://github.com/kernel-node/kernel-node/pull/86) · [#85](https://github.com/kernel-node/kernel-node/pull/85) · [#78](https://github.com/kernel-node/kernel-node/pull/78) · [#31](https://github.com/kernel-node/kernel-node/pull/31) · [#71](https://github.com/kernel-node/kernel-node/pull/71) · [#66](https://github.com/kernel-node/kernel-node/pull/66) · [#64](https://github.com/kernel-node/kernel-node/pull/64) · [#63](https://github.com/kernel-node/kernel-node/pull/63) · [#60](https://github.com/kernel-node/kernel-node/pull/60) · [#56](https://github.com/kernel-node/kernel-node/pull/56) · [#50](https://github.com/kernel-node/kernel-node/pull/50) · [#30](https://github.com/kernel-node/kernel-node/pull/30) | Mar–Jun 2026 |
| rust-bitcoinkernel | [#213](https://github.com/sedited/rust-bitcoinkernel/pull/213) · [#177](https://github.com/sedited/rust-bitcoinkernel/pull/177) · [#164](https://github.com/sedited/rust-bitcoinkernel/pull/164) | Apr–May 2026 |
| BDK (bdk-ffi) | [#1008](https://github.com/bitcoindevkit/bdk-ffi/pull/1008) | Jun 2026 |

### Vaan ([@va-an](https://github.com/va-an)) - 14 merged
| Project | PR | Date |
| --- | --- | --- |
| rust-payjoin | [#1635](https://github.com/payjoin/rust-payjoin/pull/1635) · [#1590](https://github.com/payjoin/rust-payjoin/pull/1590) · [#1576](https://github.com/payjoin/rust-payjoin/pull/1576) · [#1554](https://github.com/payjoin/rust-payjoin/pull/1554) · [#1509](https://github.com/payjoin/rust-payjoin/pull/1509) | May–Jun 2026 |
| payjoin.org | [#133](https://github.com/payjoin/payjoin.org/pull/133) | May 2026 |
| bdk-cli | [#270](https://github.com/bitcoindevkit/bdk-cli/pull/270) · [#241](https://github.com/bitcoindevkit/bdk-cli/pull/241) · [#237](https://github.com/bitcoindevkit/bdk-cli/pull/237) · [#225](https://github.com/bitcoindevkit/bdk-cli/pull/225) · [#224](https://github.com/bitcoindevkit/bdk-cli/pull/224) | Nov 2025–Jun 2026 |
| rust-bitcoin | [#5939](https://github.com/rust-bitcoin/rust-bitcoin/pull/5939) | Apr 2026 |
| bdk_wallet | [#422](https://github.com/bitcoindevkit/bdk_wallet/pull/422) | Apr 2026 |
| esplora-cli | [#3](https://github.com/yancyribbens/esplora-cli/pull/3) | Apr 2026 |

### Chaitika ([@chaitika](https://github.com/chaitika)) - 28 merged (2026)
| Project | PR | Date |
| --- | --- | --- |
| shroud (Silent Payments, CypherCommons) | [#151](https://github.com/CypherCommons/shroud/pull/151) · [#150](https://github.com/CypherCommons/shroud/pull/150) · [#145](https://github.com/CypherCommons/shroud/pull/145) · [#144](https://github.com/CypherCommons/shroud/pull/144) · [#141](https://github.com/CypherCommons/shroud/pull/141) · [#138](https://github.com/CypherCommons/shroud/pull/138) · [#134](https://github.com/CypherCommons/shroud/pull/134) · [#130](https://github.com/CypherCommons/shroud/pull/130) · [#118](https://github.com/CypherCommons/shroud/pull/118) · [#124](https://github.com/CypherCommons/shroud/pull/124) · [#123](https://github.com/CypherCommons/shroud/pull/123) · [#122](https://github.com/CypherCommons/shroud/pull/122) · [#121](https://github.com/CypherCommons/shroud/pull/121) · [#120](https://github.com/CypherCommons/shroud/pull/120) · [#114](https://github.com/CypherCommons/shroud/pull/114) · [#108](https://github.com/CypherCommons/shroud/pull/108) · [#103](https://github.com/CypherCommons/shroud/pull/103) · [#102](https://github.com/CypherCommons/shroud/pull/102) · [#101](https://github.com/CypherCommons/shroud/pull/101) · [#93](https://github.com/CypherCommons/shroud/pull/93) · [#89](https://github.com/CypherCommons/shroud/pull/89) · [#86](https://github.com/CypherCommons/shroud/pull/86) · [#83](https://github.com/CypherCommons/shroud/pull/83) · [#79](https://github.com/CypherCommons/shroud/pull/79) · [#76](https://github.com/CypherCommons/shroud/pull/76) · [#73](https://github.com/CypherCommons/shroud/pull/73) · [#67](https://github.com/CypherCommons/shroud/pull/67) | Feb–Jul 2026 |
| shroud-indexer | [#100](https://github.com/CypherCommons/shroud-indexer/pull/100) | Mar 2026 |

Plus 2025 Silent Payments work at the Bitshala Incubator: [silent-pay-wallet](https://github.com/Bitshala-Incubator/silent-pay-wallet/pulls?q=involves%3Achaitika), [silent-pay-indexer](https://github.com/Bitshala-Incubator/silent-pay-indexer/pulls?q=involves%3Achaitika), [silent-pay](https://github.com/Bitshala-Incubator/silent-pay/pulls?q=involves%3Achaitika). <!-- TODO: replace with direct PR links -->

### Diegodev ([@0xlaga](https://github.com/0xlaga)) - 14 merged
| Project | PR | Date |
| --- | --- | --- |
| LN gossip-observer visuals | [#20](https://github.com/bitcoin-visuals/LN_gossip_observer_visuals/pull/20) · [#10](https://github.com/bitcoin-visuals/LN_gossip_observer_visuals/pull/10) · [#9](https://github.com/bitcoin-visuals/LN_gossip_observer_visuals/pull/9) · [#8](https://github.com/bitcoin-visuals/LN_gossip_observer_visuals/pull/8) · [#7](https://github.com/bitcoin-visuals/LN_gossip_observer_visuals/pull/7) · [#6](https://github.com/bitcoin-visuals/LN_gossip_observer_visuals/pull/6) · [#5](https://github.com/bitcoin-visuals/LN_gossip_observer_visuals/pull/5) | Mar–Apr 2026 |
| BINST pilot | [#2](https://github.com/Bitcoin-Institutions/binst-pilot/pull/2) · [#1](https://github.com/Bitcoin-Institutions/binst-pilot/pull/1) | Mar 2026 |
| Master Bitcoin From Command Line (Librería de Satoshi) | [#91](https://github.com/LibreriadeSatoshi/Master-Bitcoin-From-Command-Line/pull/91) · [#90](https://github.com/LibreriadeSatoshi/Master-Bitcoin-From-Command-Line/pull/90) · [#89](https://github.com/LibreriadeSatoshi/Master-Bitcoin-From-Command-Line/pull/89) · [#66](https://github.com/LibreriadeSatoshi/Master-Bitcoin-From-Command-Line/pull/66) · [#65](https://github.com/LibreriadeSatoshi/Master-Bitcoin-From-Command-Line/pull/65) | Feb–Mar 2026 |

### Dayvvo ([@dayvvo](https://github.com/dayvvo)) - 9 merged
| Project | PR | Date |
| --- | --- | --- |
| Alby bitcoin-connect | [#324](https://github.com/getAlby/bitcoin-connect/pull/324) · [#294](https://github.com/getAlby/bitcoin-connect/pull/294) · [#281](https://github.com/getAlby/bitcoin-connect/pull/281) | Feb–Aug 2025 |
| Alby js-sdk | [#299](https://github.com/getAlby/js-sdk/pull/299) | Feb 2025 |
| cashu-ts | [#125](https://github.com/cashubtc/cashu-ts/pull/125) | May 2024* |
| fedimint-ui | [#418](https://github.com/fedibtc/fedimint-ui/pull/418) · [#412](https://github.com/fedibtc/fedimint-ui/pull/412) · [#411](https://github.com/fedibtc/fedimint-ui/pull/411) | Apr 2024* |
| Jam (JoinMarket UI) | [#725](https://github.com/joinmarket-webui/jam/pull/725) | Mar 2024* |

*2024 PRs predate Code Orange cohorts - listed as community-member history, not program outcomes.

### Psychemist ([@psychemist](https://github.com/psychemist)) - 7 merged
| Project | PR | Date |
| --- | --- | --- |
| **LDK (rust-lightning)** | [#4293](https://github.com/lightningdevkit/rust-lightning/pull/4293) | Jan 2026 |
| Mastering Taproot | [#31](https://github.com/aaron-recompile/mastering-taproot/pull/31) · [#24](https://github.com/aaron-recompile/mastering-taproot/pull/24) · [#23](https://github.com/aaron-recompile/mastering-taproot/pull/23) · [#22](https://github.com/aaron-recompile/mastering-taproot/pull/22) | Feb–Mar 2026 |
| bitcointranscripts | [#615](https://github.com/bitcointranscripts/bitcointranscripts/pull/615) | Mar 2026 |
| Saving Satoshi | [#19](https://github.com/saving-satoshi/saving-satoshi-script/pull/19) | Apr 2026 |

<!-- TODO: BDK Android WIF sweep tool + BIP375 Go from the 2025 report - add direct links or drop -->

### Muhammad ([@muhahahmad68](https://github.com/muhahahmad68)) - 8 merged
| Project | PR | Date |
| --- | --- | --- |
| **Bitcoin Core** | [bitcoin/bitcoin #35320](https://github.com/bitcoin/bitcoin/pull/35320) - BIP32 seed-length validation | Jul 2026 |
| rust-bitcoin | [#6394](https://github.com/rust-bitcoin/rust-bitcoin/pull/6394) | Jun 2026 |
| **Floresta** | [#1001](https://github.com/getfloresta/Floresta/pull/1001) | Apr 2026 |
| bdk_wallet | [#487](https://github.com/bitcoindevkit/bdk_wallet/pull/487) · [#476](https://github.com/bitcoindevkit/bdk_wallet/pull/476) · [#471](https://github.com/bitcoindevkit/bdk_wallet/pull/471) | May 2026 |
| Cove wallet | [#728](https://github.com/bitcoinppl/cove/pull/728) | May 2026 |
| SeedSigner (kdmukai) | [#12](https://github.com/kdmukai/seedsigner/pull/12) | Apr 2026 |

### Razor ([@RazorBest](https://github.com/RazorBest)) - 6 merged
| Project | PR | Date |
| --- | --- | --- |
| peer-observer | [#408](https://github.com/peer-observer/peer-observer/pull/408) · [#400](https://github.com/peer-observer/peer-observer/pull/400) · [#393](https://github.com/peer-observer/peer-observer/pull/393) · [#390](https://github.com/peer-observer/peer-observer/pull/390) | Mar–Jun 2026 |
| corepc | [#547](https://github.com/rust-bitcoin/corepc/pull/547) | Apr 2026 |
| bitcointranscripts | [#612](https://github.com/bitcointranscripts/bitcointranscripts/pull/612) | Mar 2026 |

### Arowolo ([@Arowolokehinde](https://github.com/Arowolokehinde)) - 6 merged
| Project | PR | Date |
| --- | --- | --- |
| Mostro (Lightning P2P exchange) | [#848](https://github.com/MostroP2P/mostro/pull/848) · mostrix [#101](https://github.com/MostroP2P/mostrix/pull/101) · [#95](https://github.com/MostroP2P/mostrix/pull/95) | Jul–Aug 2026 |
| **rust-payjoin (BIP77 Async Payjoin)** | [#1659](https://github.com/payjoin/rust-payjoin/pull/1659) | Jun 2026 |
| rust-payjoin | [#1498](https://github.com/payjoin/rust-payjoin/pull/1498) · [#1457](https://github.com/payjoin/rust-payjoin/pull/1457) <!-- click-verify merged status before push --> | 2026 |

### Gradale ([@alexgrad42](https://github.com/alexgrad42)) - 5 merged
| Project | PR | Date |
| --- | --- | --- |
| rust-bitcoin | [#6387](https://github.com/rust-bitcoin/rust-bitcoin/pull/6387) · [#6125](https://github.com/rust-bitcoin/rust-bitcoin/pull/6125) - constant-time Poly1305 equality | 2026 |
| hex-conservative | [#247](https://github.com/rust-bitcoin/hex-conservative/pull/247) · [#245](https://github.com/rust-bitcoin/hex-conservative/pull/245) | 2026 |
| corepc | [#604](https://github.com/rust-bitcoin/corepc/pull/604) | 2026 |

### Alex Xie ([@alexxie16](https://github.com/alexxie16)) - 3 merged
| Project | PR | Date |
| --- | --- | --- |
| OpenTollGate (Lightning/ecash) | [#107](https://github.com/OpenTollGate/tollgate-module-basic-go/pull/107) Lightning checkout + balance view · [#105](https://github.com/OpenTollGate/tollgate-module-basic-go/pull/105) SDK source-build packaging · [#79](https://github.com/OpenTollGate/tollgate-module-basic-go/pull/79) apk packaging | Apr 2026 |

### Mwihoti ([@mwihoti](https://github.com/mwihoti)) - 1 merged
| Project | PR | Date |
| --- | --- | --- |
| **rust-payjoin** | [#1589](https://github.com/payjoin/rust-payjoin/pull/1589) | May 2026 |

### Claimed, not yet linked <!-- TODO: verify or remove -->
| Developer | Project | Note |
| --- | --- | --- |
| Bunny Rolling Dice ([@rollingdice](https://github.com/rollingdice)) | BlueWallet | [#315](https://github.com/BlueWallet/BlueWallet/pull/315) Indonesian translation, merged Feb 2019 - predates Code Orange, history only |
| Psychemist | BDK Android · BIP375 Go | From 2025 report - add direct links or drop |

---

## Open / Under Review (24)

Link states re-verified 26 September 2026 with `tools/verify_dashboard.py`.

| Developer | Project | PR |
| --- | --- | --- |
| Peter | kernel-node | [#32](https://github.com/kernel-node/kernel-node/pull/32) |
| Mwihoti | Saving Satoshi | [#20](https://github.com/saving-satoshi/saving-satoshi-script/pull/20) |
| Chaitika | shroud-indexer | [#103](https://github.com/CypherCommons/shroud-indexer/pull/103) |
| Psychemist | BDK devkit-wallet | [#53](https://github.com/bitcoindevkit/devkit-wallet/pull/53) |
| Dayvvo | Btrust website | [#25](https://github.com/btrustteam/website/pull/25) |
| Peter | kernel-node | [#108](https://github.com/kernel-node/kernel-node/pull/108) · [#107](https://github.com/kernel-node/kernel-node/pull/107) |
| Chaitika | shroud | [#164](https://github.com/CypherCommons/shroud/pull/164) · [#162](https://github.com/CypherCommons/shroud/pull/162) · [#161](https://github.com/CypherCommons/shroud/pull/161) · [#160](https://github.com/CypherCommons/shroud/pull/160) · [#148](https://github.com/CypherCommons/shroud/pull/148) · [#135](https://github.com/CypherCommons/shroud/pull/135) |
| Arowolo | BDK (bdk_wallet · bdk-ffi · bdk · coin-select) · Mostro | bdk_wallet [#571](https://github.com/bitcoindevkit/bdk_wallet/pull/571) · [#537](https://github.com/bitcoindevkit/bdk_wallet/pull/537) · bdk-ffi [#1119](https://github.com/bitcoindevkit/bdk-ffi/pull/1119) · [#1114](https://github.com/bitcoindevkit/bdk-ffi/pull/1114) · [#1102](https://github.com/bitcoindevkit/bdk-ffi/pull/1102) · bdk [#2261](https://github.com/bitcoindevkit/bdk/pull/2261) · coin-select [#71](https://github.com/bitcoindevkit/coin-select/pull/71) · mostro [#896](https://github.com/MostroP2P/mostro/pull/896) |
| Muhammad | bdk_wallet | [#528](https://github.com/bitcoindevkit/bdk_wallet/pull/528) |
| Diegodev | gossip_observer · b4os-bitcoin | [#12](https://github.com/jharveyb/gossip_observer/pull/12) · [#5](https://github.com/danielabrozzoni/b4os-bitcoin/pull/5) |

---

## Emerging Contributors (First PR Imminent)

Four contributors below have verified GitHub handles and are included in the summary. The prospective entry is retained for pipeline follow-up but excluded until its handle and target are confirmed.

| Developer | GitHub | Target Project | Expected |
| --- | --- | --- | --- |
| Captain Levi | [@SIDHARTH20K4](https://github.com/SIDHARTH20K4) | BDK | Q3 2026 |
| Yongki | [@ywiyogo](https://github.com/ywiyogo) | Bitcoin Core (C++) | Q3 2026 |
| Ilie | [@Ilie27](https://github.com/Ilie27) | Bitaxe / Stratum V2 | Q3 2026 |
| Elijahhh | [@ElijahMwambazi](https://github.com/ElijahMwambazi) | Lightning Network (Rust) | Q3 2026 |
| Mr Miyagi | *(handle pending)* | Rust Bitcoin OSS | Q3 2026 |

---

## Monthly Tracking Log

### September 2026
- Re-verified every linked PR with the new `tools/verify_dashboard.py` (now run weekly by CI)
- 10 PRs listed as open had merged and moved to merged: Bitcoin Core #35380 (Peter) and #35320 (Muhammad), kernel-node #78 and #31, corepc #547, bitcointranscripts #612, hex-conservative #247, shroud #118/#123/#124 (+10)
- 23 PRs listed as open had been closed unmerged and were removed from the open list, per the data contract
- Alex Xie's 3 merged OpenTollGate PRs now have direct links; the BlueWallet translation claim is linked as pre-Code Orange history
- Added 25 PRs merged since the 12 July cutoff (Peter: 12 kernel-node + rust-bitcoinkernel #213; Chaitika: 8 shroud; Arowolo: 3 Mostro; Gradale: rust-bitcoin #6387) and 17 open ones, applying *How We Count*. Excluded as out of scope: Stellar, Cardano and Docker projects, plus two repos whose Bitcoin relevance couldn't be confirmed (Talent-Index/tangaza, beebozy/fiber-diagnostics)
- Merged total 96 → 131

### July 2026
* Full verification pass via the GitHub API: every merged PR now carries a direct link
* The April baseline was substantially undercounted. Link-level verification first established 88 merged PRs; follow-up verification raised the linked total to 96.
* Newly verified merges since the May report: Arowolo's first rust-payjoin PR (#1659), Mwihoti's first rust-payjoin PR (#1589), Peter's Bitcoin Core #34885 + kernel-node series, Psychemist's LDK #4293, Muhammad's rust-bitcoin/Floresta/bdk_wallet run, Razor's peer-observer #400 & #408, Chaitika's 17 shroud merges
* Attribution note added: PRs made before a developer joined Code Orange (e.g. Dayvvo's 2024 work) are marked with * and excluded from program-outcome claims

### April 2026
* Dashboard created with baseline data from all cohort graduates

---

## How We Count

* **Merged**: PR accepted by the project maintainer - *direct PR link required, no exceptions*
* **Open / Under Review**: PR submitted, not yet merged or closed
* We count: Bitcoin Core, rust-bitcoin, BDK, LDK, rust-payjoin, Floresta, peer-observer, wallets, Lightning/eCash infrastructure, and Bitcoin education repos (marked as such)
* We do NOT count: PRs to a developer's own repos or forks, or non-Bitcoin projects
* PRs made before a member joined Code Orange are listed with * and excluded from program-outcome claims

---

*Updated monthly. Code Orange Dev School | [codeorange.dev](https://codeorange.dev) | [github.com/code-orange-dev](https://github.com/code-orange-dev)*
