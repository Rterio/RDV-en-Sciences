#!/usr/bin/env python3
"""Télécharge les images de l'ancien site Google Sites dans le dossier images/.

Utilisation (depuis la racine du projet) :
    python3 scripts/telecharger-images.py

À exécuter UNE fois, pendant que l'ancien site Google Sites est encore en ligne.
Les fichiers existants ne sont pas écrasés (supprimez-les pour les retélécharger).
"""
import os
import sys
import urllib.request

G = "https://lh7-us.googleusercontent.com/sitesv-images-rt/"

IMAGES = {
    # Accueil
    "images/accueil-banniere.jpg": G + "AMxu72t_cYfVB3_Pw_RmYoGw3inrbeKIpX-vpCnFam_B1V2HV4V8g_-fx-8v-zW-rcjPniHSLpdD1AU843vd2yyZ01KW20r1vr48xfhJEkHGnfc5cChwOWegLvTYdEA-MEKS7srsNyqv0sdUrtZhu8IsbCL1OBQcTcokZdQfjBrcM7acYwKPZUUghGwja2PfRH_WR7GQW1kUI8xlPWpKz9v7VtTSyahfLeq5VsspgAiwuD4=w1280",
    # Activités
    "images/activites-1.jpg": G + "AMxu72v0EpBCeCZZQR9-HULsvEMvSI2MDEJRKUJs0vLP8oU7rHmoh40N-ZY24G4biSd8I9JxqRvpGFfbVEmQ_CArZ7XwAVr0zwtJP7N79TQTOyA5uZ-GED_kWwSPlpqEqAVNrzWtPMylBf5hEbMAtUi_bn0SWimFc7X_U8rMADOIl39YzE0J9vofB4ZL8bbbfY-Avpk4lhB73yjJVvMILQvNJ43F0MEyl-tAs-vNDvuHdBo=w1280",
    "images/activites-2.jpg": G + "AMxu72ucr-zaRJeRreSYcGAOYUlEv_kd5zYDQ-Y_10PUzW_5ykGhKqxlqBHMKmFrQY-MA5D-OfjdMy0ON3fp_XbW6GxjszuBS1XRqznJtSQp8ZM_QP6t26QAjDaUjioTQ6c-ke5LVl-BI3A3T_S2w2m6RPxwl05gzWMce9FW4qIm1IZcVv26-qboO3hA6f9TDKNwoUQwWIVyMTNpjyx6q8ZpKZhkPEeF3eUNQEwyfT7_YYs=w1280",
    # Partenaires (image en bas de page; les logos ne sont pas récupérables automatiquement)
    "images/partenaires/bas-de-page.jpg": G + "AMxu72t3pWSIfs1B8M--iCdYCVleBAQi3mcp8A3Vtgy06eTXV7zdRZ_JM4xJRZOxeBui5DKin4PQkE1q9W-yakCwamzv_RpUxhMypujdQl3BF-3UZzvrJk3wGRmy6BgY8jJ8WF1KAT_CW5cQ6rNmnptzB-mUMsRCsgNfirZ_kbU3j5ofPYEERaZqShjRddieNw55yqJ26KkrUX8A3aHgdtRTV0aWfcdROfPOfh4w2MvR=w1280",
    # Organisation : comité
    "images/organisation/zoe-jargaille.jpg": G + "AMxu72t8-snxITAhHHY_HnKKqgst0LlRT9uvoTB4NR0e-Ta0H1uMe96kgETVTsdMuL3d1-tEIxYJFJZKEyEfyQbAMM1Rj_VCvB5J11k2OSj3pdO3d9Isso50qYohs3Fuwb1DILamzL1ATS4R6qRWdoX33KT2uXpDYiyU5sTZdXpdzr069yhlPfAXZ_7ServxHACMiAmJSr8VzYMBGAf_Hlq61GqttAlr7nHAf4hxqaLg=w600",
    "images/organisation/ludovik-levasseur.jpg": G + "AMxu72vYX0boU9qMCD7hFqgPyPv081vCeiD_4r-JlsPoGRxS_4Gk1hmtdQuR6fi_1juoWgBrH9rFN7QQjxUOk_lBSvtlN1MNvKIyPOiEELtrOCzl1Bgp1f74MDWMv1fBydsfY4GRFVw-1VSL8LZCWKvnJW_pohkBov6Y5b_F9mFJwcFbhUOkbZ7PsZXPvOTGAavn7HzQ-lBrxQLpx35EcFdxSGmQjlNaSKA6xzV9Eoy_7FQ=w600",
    "images/organisation/hiba-arfaoui.jpg": G + "AMxu72u0NoeVA9vof_pyQLobkYfpxpRnQVcWwlUbhYRzshVeV1YHbenxsZHZX7uqh_RqJM0gJmuWl7eqcGQhF1-ogQn6RGSseBlOwdjJSu_Z066rpyS5RtYwZDBIX7vjTX8zSiUC7hGs1NJLQvhY5zeOlBibeBozuWkyxBlbck9LxvXWyehKh5ytnk4Dkinr48wWtpz3IuoKkM-j74dutFXTVhO673GZvNQsCu7xRc8El2c=w600",
    "images/organisation/alexe-boisvert.jpg": G + "AMxu72vHmM1rY-lbwTzTBKdvUZW9Dek8wSyzgTmDgXKrtjNjfPXduudENS0vB94iM6cXrLgKW9rJTAFwa9d5Xq4XhU2-u0A1Iqw--xpVB3upuhhfAAaQod0dgdeX-d5mNWHeUBIXp06E_nVMtrbZ5LGZf4YRwH3Eq3XINtz-1OxxcK-gEC-UK2d69FkH569UiWgiz_tCRoPRYrLGDMzfE7W-EVxxo0LNi1X6fqTBliDskYs=w600",
    "images/organisation/laurianne-gratton.jpg": G + "AMxu72sdipAi-x_Hi4ZSfVOTliUBN_h4Us-OupYK_hpodDqXwBB3OedLPkaidzF_2SqS8E8kerD-vebxIh_0Az6AcDpFjobNdaNxeHT4_KDdCtsN-i3W5EECddlPOiNqXl8rd8QNKjEMNMBLsF466eVkaFlNF2m1M0_o9cVYi79RIRlIT7bLtfUo38S47ZoBOofJbzVgI2n0TJunS6C2E55Hl14nS0xyS72BlVAOWCoytRo=w600",
    "images/organisation/marianne-tremblay.jpg": G + "AMxu72vfD32My_hH1iMX09lDAXtLA2s94SX5oHHd39JpUw8fD2kpprc2lj78fe6bbK8N75ESj6-1ZcWLH6gNEBAgZK3saCHCkDlm9L-j3ImWGkS-H0iofSYhY5GD0tbAgH206DXq65TGxEJ_x4e6hLmj4f8vhukUExEF49NbGD15fKbLD840_wUysjHsy0P3=w600",
    "images/organisation/mariane-gosselin.jpg": G + "AMxu72sad6n_Jpsx_4jT8bl9EGh4dDvqQDEDTe1z7mcabUrH2R0Pxd9_6aqlN6eaExtce7xmCHr-JAP5C1bYcbValTiGRZk3yLOldQZpGWDIJeFNO1krR2e7f4f2D70EnQKwjPXZgvOB3aCL3B-nJIlvGaB_07aKrV1Rod8yx7cRX2bTfbxGjKOCeM1Ws7WWfITkZGJXQ1FIYA3wYKbOE2BqjJShAlTn_KoNd_EwB3tI=w600",
    # Organisation : directeurs et directrices
    "images/organisation/melissa-st-pierre.jpg": G + "AMxu72t8L2m77MD6FjIFqACnEJagn2tq-MYC6yxX2QQAklbC9SghjjmUSSb-qqwv9znFsVxW3xtGZoGrcJEhK_gQMT0LyOS7B6Mh0LoXuztqonB1OG2mCmFPel22JGjhYCDX69qf25h0qSsjhfMPIwgBJE8r2C-cuVilIqMqjK5REgWn_D8YUdrObvt0OX4-QQdv1wb5kCJ6YgEoSclxEtYrNYQooyJz_yq3GV-N7W6g=w600",
    "images/organisation/laurence-gagne-girard.jpg": G + "AMxu72tPcUXy-r5hoiFBqGtKR7LXI48G4Yk28eiT-COPcerVWTfBjP88zRlYe59LNqq3KcqUIBOE9n9Lp0hC7SZTY0kAyZtoYUtTEfK5MsSLVHdZGDk1-bEabyrj8A1icWdyS3Xbx3iymXf2r7AUkPs0qo9Vyz6_HeAJp0wLlNdcaOt2C8NkL_-FpqRfjvlLcxNYy1VDI0bu7rUVW0USlpvfr7LyPkwmg2fDDOM5QyUGKG0=w600",
    "images/organisation/lara-aguiar.jpg": G + "AMxu72scrYMD-L8EQTCvm2fPQZcejkNnGbRGVQj-hX2qIhgyXWZ8C-tcMM26S8AxfiY7_efzYGLmyORAy5JxkcwENN7F7Ulvv7CPjQVnhQMtU19UgX-5CV49BpwHQVMROJHQPYrgNLGkDRQNCHzH3Hm2pzg3XUprRQl6aNNqTEI-pY8iadhz2kN1EIkgaYUy68pjDJ66wTQXY1O98cHDLn67vrtgiYOW8F8PnaZZ0NRNdww=w600",
    "images/organisation/lyanne-begin.jpg": G + "AMxu72tGr7ybmNJFoC3MK5FDrgs7Kx9xHA2xmbYOLj2eejH9BjKORCauznlYqB9xjAQ3T17eH30gGznKQuZkouD6_jXArHkf4HDwq51CKjKDcX_sVZCz7ua3323mNvc1lYMDiSzwca3YVGnstx5ak5vatdkZdOShuHcR4GXINJH1GaNBEC0pJtyviK6RolTuIw0A2zAynNuK5PRgJOkwn7BPbKs5WIOPSE8syklnccfJ=w600",
    "images/organisation/felix-veillette.jpg": G + "AMxu72s8jiH-N2sT2y-AxpAago2Vfi6aDr-ol_PKxK3JxLdfwiChu9Fo1AkDW4otHOtyG8tOKaaMxYjPlCclaCbnc-H0HDOswDIkNwSqEfYEZOchVXGtvNLOLLY3ggwDpK8WcfC1gykklpDFEXsnlllRD564yn_6uMv-SoDNnff2ksw-1cOs_iMmnmfVHcXt07dST5PgryJmfBiw8wQyb9W5JSsDpfSc1VxSqPKcRAY_rNM=w600",
    "images/organisation/antony-martel.jpg": G + "AMxu72t1Y1OLcbuolp9PeomaMG0W7iYqnJNsuZIbGbGiq_lCgfLED9IziBIyd41d1hwIBfo0UMN1I1Gikx-6uo7gwQS32hzvmao91TasnMOGTSzaHlVlUtFhICkJpW4yqwx8QMKanV9gQlyv7c3G1ok-t9-tA3k7vcEUfXbkBBkCpup6XvhUMYIWzT0O4ahtdUK1RkVlEahR3reFV0gEcevlk5S3qqohPW-D3ODq4bTMHbI=w600",
    "images/organisation/laurence-legault.jpg": G + "AMxu72sDJioMAUqUvhuXaD867-j8w1Mfx4kVcFQ7zMVEkfDDTr1TBjdxkJ5-6wYADit13jcuFFzwyz__-fY3GQxVZVOzcqkWGitvtmyOOrkcceJITs6GBtG749LXJlXfuMdHPq4kM-sFX3bjjwkytwtV3u_lljmyU7g30aO5Ed2f5tVndeR6HdG6dxCj90Lc3kaME3TjpNjFD_n-gQUxIUcxtNdNAuJHsIbzzR36w1zAPsk=w600",
    # Édition 2025
    "images/editions/2025-01.jpg": G + "AMxu72v_NOt7QVHF5LHRqdYmliTxXABffP7RZSmL8T5pSVlobae6Ybj3SSippDdk7IsGLZNLbr5eSjalPJQ1YAoBLKuJ-2EAdPraIyAMyuc9n_afctk7MQy9kM4FVgjjeBUkY-BepYPm6fSkZv_s_jSKAg2pjb8Cv6TtE4Z1v_MbK40qKs0sQPVKCAd5KAvXP70ho-FJQojItNgHPxs0NJFPSh2qGirrOL0FtDs49t03DYs=w1280",
    "images/editions/2025-02.jpg": G + "AMxu72t5tUsuODuhgchfWzDAFfR3bgPtJzbPEbas6HMSN4NT5811vyEagBKThAgSdaAm0AfUZzaYTzmYSQGD5NhD7_oqx4uTjU1-POucBAKQfg82fQNFbgyXyLN_1lv_0wg4zkA7s4uS9SWTkc5gCzwNOJi4GplIF5NSBSpTheurR15UKezgjHh0x6icbtQfLCCYHaAffZeRm4GUD_NT5nWQaByi4ab6FTmZC4ILPTq1=w1280",
    "images/editions/2025-03.jpg": G + "AMxu72tu5KPxSdo5EFrPXZ-rwGYrvaisldHTx_gJfrB2Ru2fRQDzK6moddowGAxUliiRYFarCWQedyFqvtrzyXYXDXMmIITj59w7BYwBy9m54XgNzr48zpHWXSQsTZmASx7GNzr4qiRXuhZMMOvUXYLuJkES09GlSmA58VXMlk2rLk7KGqhsdsH0UmM8CYFKPJnxUCszDBDtRHn3wCJKyfg5TKUIr1QjDqkhR8CgwBBWL3I=w1280",
    "images/editions/2025-04.jpg": G + "AMxu72uB4Q6f0mXSwGgjYlW9ydM49oQbCVrv4ERyjztwoTEh3Gj4htowdbKxn5KEqJjMyI7O7142wE5Pn4KgR9DPfgNTrnPU632ivI2n0aXSL7cQCTO1SGCamB8O_dydUyE91u4LiYlBGHUua7Z36lvN2uIOQMoF1k7ru4eWiqMm5NFnn0Z8ddwpzdPRiNZvAtyDidyEDh0DkAGaiW2ZwLekIfP_olobL3iT7wTgZI8ubmc=w1280",
    "images/editions/2025-05.jpg": G + "AMxu72v5c79yA8pWH8GdD8j3ACyUPB9BQrRjUtC3j9A3D6mycmRu9fbYlgmJUj80bMHAwZpMG8omrcDrLvx_Xd_XkoW32VURwov46mQETLE3S4qubxcvPaiQR7tZo3X5MYiMLYXgAv6-2QFr-GILrFJcW8m_VnvVcCEmFkVrr3h3vfAk7FNfJFDhY76ahrewUoI-xxm9saa6lEnnQPWCL2eCShp67_LLQDlGkpx8frmPfz4=w1280",
    "images/editions/2025-06.jpg": G + "AMxu72v6n0XhkvKrPIUqAf_8FaQdgTtILhtW7s83lAySTi6Wd4G-WNzVgj1A0_dDA5xigHD0zLew4N2s0x05fdip_FKOX5UN5MsB9xYYJNcl9khD-ej3l5DX-egRkUarn39qQ1i7QeOhRWB1uyYswxiyucYSMi7EqZttuC8Qqnj6Ok2CEAR8vu0qsY_fIlz1YZzEFDS4Z4prEn5w6t4tI0VHxW845tKdRm9UMxl5BDRq6qQ=w1280",
    "images/editions/2025-07.jpg": G + "AMxu72sNCt1VGOTD_z3Y8coO6_D57bwrl3ly0k-t5_2XrAhMDjK-10KqSHIW_KDQTb494x_JcUlMUB11NDoRco_2y2pHWex3UKRSIDNeziQp_tFRz8xKRcer9PYPHZ741gIHF_f4zUUoNE1ik4WKvHmbN1tPghuneYqixGEt8Vc_VNxO_izDh7eqbd0-ENHE8ri4tSI0U_6w9p4AHVljsD9pqSOwVhcUjZ-MvzOvHFnr=w1280",
    "images/editions/2025-08.jpg": G + "AMxu72sYwUn52KRn4HHtCv56_-xqYGMNzGXAMQrOWlbGDO_GMADBhYI3fGG5fkB1_AIbIx7jV52oY_ozzcD6UjPTjTMgu0pCSGszJG9yK7ohtL6Ycf2ApY4GXqgNu7DLiviRgPcpmwZGjn4YSJqD-uGMCZBHpcXUfYDFmHUDi018kMMnp3lc4QoRmGLI_9KwO9PqftxB6aPs3L3ZF-Lg3qSVUZF4CUEo3LxfgPiT95PpOeg=w1280",
    # Édition 2024
    "images/editions/2024-01.jpg": G + "AMxu72tewTVSPgGzA3OZ-cQqdjK9hTIBDhBQKqML7LvOECQnOaVLNX1a2NWRYVjJZRiyTGwugcvVYAQwjAqKcpsKB5jTJVVRmG29LIAAy8GOuIMJTtPUW0dP493L1FQP5lwSQRZDWi33v5DuUiNlDkenALPPyqjBLsK4Z708S83c6A2PjMVx1Nrx-d64WBcePG-HQ2nC2MIFpvL07VBz3ZEUwuk4CL4oPEeJhp1QrJa2wY8=w1280",
    "images/editions/2024-02.jpg": G + "AMxu72vdisFu7jPzPjr5vKRJQ65ZYU6tBwZB7NTiSiLJ_Si_ajV4Brx5kM3OsJRoZ2Zwltvpna6t5oJ88o1Vjf-EnQnVe5h5TVCi0QujuWojTamIJgkmILeIN5AgaOUyd31ctvO_YU22JR6aaJ6aLQvQGoF2OT_nXORuryiZom-98sQAosozGyauYxNJPn7sa3IKjVoXxVS8wUbNDxVKISsOJka4l83s-Wi8IAPvMc6w570=w1280",
    "images/editions/2024-03.jpg": G + "AMxu72uTvRB3-ePxUXyCB9N6MQRvarOS0tj3zx9fcaoUcCW77AkY0aiyApjaeq5BoAycI6WHG9kHZbHw9o2bIqlfeEp3rJk4VFScDqzRgfoIVke_0SXwYMQaLQYN1Z7soZEB3EvTMGshA8HnIucnorLZMqCUQhE6SbhyAzCE6uxFY0ypm0cxSxz3q562FNH1hNBQKoStzaFuRccESqzBoNqBzUvWK_e2hlnmYz3SiP5HaxE=w1280",
    "images/editions/2024-04.jpg": G + "AMxu72ty3BkmgdhwLmmbZBzY-RGKdeyWxRwJa2UvG1IFJYE9Ra0aAVSFqNSvCPBfkA7kTkgp23Ro4vnND8ZFhE-CML5E2nCWvhwPxggUtfzIflS8Ia23mZsF0qm6ysazSM_JE2dLBx8ti_Vm2I_Q39h0fn3dUriTKas4LeYTlf_3Jg0iI5QMHQk7rjY_a6fCgrJ9TYSPG1AHiiAi0j4a_KDIgYneVSUD-JYB6v71K3v7Bxw=w1280",
    "images/editions/2024-05.jpg": G + "AMxu72v-qB-jCAZG8Hj7bus_oajbBsKOwNRZsqU_luzvMUS48QGiEppZAMuEdt01EnjElWqe_zIDS1drI_DENmPdyzmB6_e9v14Mzqp1B-ErrKL35QMPg4CtDE50KRCKHwT1C0ocvTqAM-4Zt8X4yrS2yhrudrcc9tS-P2imVX1hj3B1S-E13PmcyDi9I64AwsctBzX6OvMSNH1_DH8Hv_1TnIIYuk2LCSdoej5hlzYV-dE=w1280",
    "images/editions/2024-06.jpg": G + "AMxu72vdIlDPHfLv5ia0j2gbMI25d_Ep31gLmMD7bi3QPMnXum7_H-qJTVkxnCZyuSBCipeBqu910LldbOpPijf8e9KeJuY6kX5ndXFBU8akRURq4sRPIbt16vx8WesZS7mPnas2OjMdI8NXoNYFhUrthRS5KKWDVVVqR57kVg_ZGdt_YmOKxyr3_joGMzrrWPHk1lstYxawY7L7VMz5cG87zBPRULXnz9uO7mFnuiHh=w1280",
    # Édition 2023
    "images/editions/2023-01.jpg": G + "AMxu72v5V3tLbEIFHloAlVQDwDwP13cLBGtSiLRxA4hgRHY3IkhIFjG50mS5b-3Ds0Kl8jHyLhX99OFOofYfC4O4y2I4uhl81UoJlfeGhdW6tSV3_OdcDX0zC_NfipYP7YvVVF0-owr9Lk2wSQrF923q_UzkVo0pqiA9S-Xc1sBP109xQl9kxErS_PVr_MvzJCfX5171JfTRU7OofQDHuU05g6P_gvbXHuTnW570RkizAfU=w1280",
    "images/editions/2023-02.jpg": G + "AMxu72uOrxp4TWLNd2oDeolMMiB9Cz02sijpae3Kj6xp9X5a4BJkskDR67nx6g-3KxPXlP3tWSQ1hf6USCMKLFcb9vtUy5DRtF9GNzQZv3b9_TYPR9ZpHJ5nPf2l5fTqQmuKUIGAyPXjcUyiHtr7a8dzJY0YDaVG4MFuK428t8HqNRQRUFmkcZ8N2l22RXyXuU3m_CwI8s_Qlvan9nNPErtK7NLB1v8W1QdXqlYFnL-p=w1280",
    "images/editions/2023-03.jpg": G + "AMxu72sGftSC07pAlZIRGQ4dZlByxSi87OPH7KWiKlixfsN-L2EoZHg8z_Vc7TLYXjo5hydKFB-AnG61vpk9dRXH6_BARp2-7Tp_jdbkvE4nMQSxLu8jsmFQ_NEnPu3HN0em2V02T1XTI0_6oA1wH0mTtIGYXI1hDX1tCOMadMe5gc55bQMwvOAtMNn2lwtD7VdJv9uiBwnnltCVHnmolgt92eN1stojPGsXmKxU5TZJrAE=w1280",
    "images/editions/2023-04.jpg": G + "AMxu72uxIiF0btnYo8EiYp5i39MC4BtWRkoAYFcT_MxvjwufLvdrg31XJIpsH2BB9tJSSDML39FC39B6g9Dsq9kOFgFDscW04jnMRM_odrgAiwqcX9zAGGwMvH-5krMuutnisvYk1Q3iEXXkVezY0XgLHv-5W9O3jaJDBTnyWOuB6QqHJuK4Jso03AqBCK4x0K017aPsLWnww9w894rb08cjH-W9CHckNQAVJedCnUWbvic=w1280",
    "images/editions/2023-05.jpg": G + "AMxu72sZ0RYdAictsWwBb2d9VyBxY9yoJj6W1xrlM2GTvKe49Yr29XpwDkGKRZa6SVvrt54xZ4eH6zY_TCJbSYkm9dBAzpAWcG06zJV0CgW6wRma5miGA7RIT4hn6wyf8qyljHkQvsZ93HbhoYfWDSGj502d_Gn6GRMhg9FnJkEcSOkr0DMNq5U8TpogMsEtCwz03v1BvXm6y54zaY15IaJgGjX8Gpn8SwAD39TvVUaH=w1280",
    "images/editions/2023-06.jpg": G + "AMxu72suAAl-iSUiNe72BuQgdWC45uODvC8aVn51lZOLk8CtvPp8KtQ9ziluXjAW57Sb5BkxL5VxCFNmR-9GkXLeKm5zni9qyNoKdB7zOPZKIlzVan4glpdKj6zLPwtbEjdhlD4D6__iadeRtdjRSa8PvYUtSE_aocd7TFskAzyyOYBolJmEj500aUHaswfieAzxqhCnoCUgUyzqBb5hqDP4qiOXr3BInhy6aykUcGUjtNg=w1280",
}


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ok, skipped, failed = 0, 0, []
    for rel, url in IMAGES.items():
        dest = os.path.join(root, rel)
        if os.path.exists(dest):
            skipped += 1
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
                f.write(r.read())
            ok += 1
            print(f"  ok   {rel}")
        except Exception as e:  # noqa: BLE001
            failed.append((rel, e))
            print(f"  ÉCHEC {rel}: {e}")
    print(f"\n{ok} téléchargées, {skipped} déjà présentes, {len(failed)} échecs.")
    if failed:
        print("Pour les échecs : ouvrez la page correspondante de l'ancien site, "
              "clic droit sur l'image > Enregistrer l'image sous, et placez-la au chemin indiqué.")
        sys.exit(1)


if __name__ == "__main__":
    main()
