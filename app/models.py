from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # タイトル
    title = models.CharField(
        verbose_name='タイトル',
        max_length=300,
        blank=True,
        null=True,
    )
    # 著者
    author = models.CharField(
        verbose_name='著者',
        max_length=100,
        blank=True,
        null=True,
    )
    # 出版社
    publisher = models.CharField(
        verbose_name='出版社',
        max_length=100,
        blank=True,
        null=True,
    )
    # 価格
    price = models.IntegerField(
        verbose_name='価格',
        blank=True,
        null=True,
    )
    # ジャンル 選択肢（固定）
    ganre_choice = (
        (1, '文芸'),
        (2, '教育'),
        (3, '人文'),
        (4, '教育'),
        (5, '社会'),
        (6, '法律'),
        (7, '経済'),
        (8, '経営'),
        (9, 'ビジネス'),
        (10, '就職・資格'),
        (11, '理学'),
        (12, '工学'),
        (13, 'コンピュータ'),
        (14, '医学'),
        (15, '看護学'),
        (16, '薬学'),
        (17, '芸術'),
        (18, '語学'),
        (19, '辞典'),
        (20, '高校学参'),
        (21, '中学学参'),
        (22, '小学学参'),
        (23, '児童'),
        (24, '趣味・生活'),
        (25, 'くらし・料理'),
        (26, '地図・ガイド'),
        (27, '文庫'),
        (28, '新書・選書'),
        (29, 'コミック'),
        (30, 'ゲーム攻略'),
        (31, 'エンターテイメント'),
        (32, '日記・手帳・暦'),
        (33, 'その他'),
    )
    ganre = models.IntegerField(
        verbose_name='ジャンル',
        choices=ganre_choice,
        blank=True,
        null=True,
    )

    # 販売形態 選択肢（固定）
    selltype_choice = (
        (1, '紙媒体'),
        (2, '電子版'),
    )
    selltype = models.IntegerField(
        verbose_name='販売形態',
        choices=selltype_choice,
        blank=True,
        null=True,
    )

    # 購入日 日付
    buydate = models.DateField(
        verbose_name='購入日 日付',
        blank=True,
        null=True,
    )

    # 読書状態 選択肢（固定）
    readstatus_choice = (
        (1, '未読'),
        (2, '読み中'),
        (3, '完読'),
    )
    readstatus = models.IntegerField(
        verbose_name='読書状態',
        choices=readstatus_choice,
        blank=True,
        null=True,
    )

   # オヌヌメ度 選択肢（固定）
    recommended_choice = (
        (1, '☆'),
        (2, '☆☆'),
        (3, '☆☆☆'),
        (4, '☆☆☆☆'),
        (5, '☆☆☆☆☆'),
    )
    # オヌヌメ度
    recommended = models.IntegerField(
        verbose_name='オヌヌメ度',
        choices=recommended_choice, 
        blank=True,
        null=True,
    )

    # メモ、感想
    memo = models.CharField(
        verbose_name = 'メモ、感想',
        max_length=500,
        blank=True,
        null=True,
    )

    # # サンプル項目1 文字列
    # sample_1 = models.CharField(
    #     verbose_name='サンプル項目1 文字列',
    #     max_length=20,
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目2 メモ
    # sample_2 = models.TextField(
    #     verbose_name='サンプル項目2 メモ',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目3 整数
    # sample_3 = models.IntegerField(
    #     verbose_name='サンプル項目3 整数',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目4 浮動小数点
    # sample_4 = models.FloatField(
    #     verbose_name='サンプル項目4 浮動小数点',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目5 固定小数点
    # sample_5 = models.DecimalField(
    #     verbose_name='サンプル項目5 固定小数点',
    #     max_digits=5,
    #     decimal_places=2,
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目6 ブール値
    # sample_6 = models.BooleanField(
    #     verbose_name='サンプル項目6 ブール値',
    # )

    # # サンプル項目7 日付
    # sample_7 = models.DateField(
    #     verbose_name='サンプル項目7 日付',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目8 日時
    # sample_8 = models.DateTimeField(
    #     verbose_name='サンプル項目8 日時',
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目9 選択肢（固定）
    # sample_9_choice = (
    #     (1, '選択１'),
    #     (2, '選択２'),
    #     (3, '選択３'),
    # )

    # sample_9 = models.IntegerField(
    #     verbose_name='サンプル項目9_選択肢（固定）',
    #     choices=sample_9_choice,
    #     blank=True,
    #     null=True,
    # )

    # # サンプル項目9 選択肢（マスタ連動）
    # sample_10 = models.ForeignKey(
    #     User,
    #     verbose_name='サンプル項目10_選択肢（マスタ連動）',
    #     blank=True,
    #     null=True,
    #     related_name='sample_10',
    #     on_delete=models.SET_NULL,
    # )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
#       return self.sample_1
        return self.title

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = '読んだ本履歴'
        verbose_name_plural = '読んだ本履歴'
