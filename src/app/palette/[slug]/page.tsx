/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { Button } from "@/components/ui/button";
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";
import "dayjs/locale/en"; // Load English locale
import Link from "next/link";
import NotFound from "@/app/not-found";
import InsertLikes from "@/components/insertLikes";
import {
  CopyToClipboardHex,
  CopyToClipboardLink,
} from "@/components/copyToClipboard";
import { getDataOnePalette, getDataSingleTag } from "@/app/actions/getAction";
import type { Metadata, ResolvingMetadata } from "next";

// Add support for relative time comparisons
dayjs.extend(relativeTime);

function hexToRgb(hex: string): string {
  // Remove the '#' if it's there
  hex = hex.replace(/^#/, "");

  // Parse the hex values
  const bigint = parseInt(hex, 16);
  const r = (bigint >> 16) & 255;
  const g = (bigint >> 8) & 255;
  const b = bigint & 255;

  // Return RGB string
  return `rgb(${r}, ${g}, ${b})`;
}

type Props = {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
};

export async function generateMetadata(
  { params, searchParams }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  // read route params
  const slug = (await params).slug;
  const Dataa = await getDataOnePalette(slug);
  const color1 = Dataa.color1.toUpperCase();
  const color2 = Dataa.color2.toUpperCase();
  const color3 = Dataa.color3.toUpperCase();
  const color4 = Dataa.color4.toUpperCase();

  return {
    title: `Color Palette: #${color1} #${color2} #${color3} #${color4}`,
    description: ``
  };
}

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const slug = (await params).slug;

  const colorsName = [
    "sage",
    "beige",
    "brown",
    "orange",
    "black",
    "navy",
    "maroon",
    "peach",
    "yellow",
    "purple",
    "red",
    "teal",
    "grey",
    "blue",
    "pink",
    "white",
    "green",
  ];

  // تحقق من طول الـ slug للتأكد أنه يتوافق مع الحد الأدنى
  if (slug.length <= 10) {
    const tagg = await getDataSingleTag(slug);

    if (tagg?.length === 0) {
      return <NotFound />;
    }
    return (
      <section className="w-full flex flex-col justify-center items-center">
        <div className="w-full h-full">
          <div className="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 animate-out gap-5">
            {tagg?.map(
              ({
                id,
                color1,
                color2,
                color3,
                color4,
                created_at,
                likes_count,
              }: any) => (
                <div
                  key={id}
                  className={`flex flex-col justify-center items-center`}
                >
                  <Link
                    href={`/palette/` + id}
                    className="w-full h-20 rounded-tl-xl rounded-tr-xl"
                    style={{ backgroundColor: `#${color1}` }}
                  ></Link>
                  <Link
                    href={`/palette/` + id}
                    className="w-full h-14"
                    style={{ backgroundColor: `#${color2}` }}
                  ></Link>
                  <Link
                    href={`/palette/` + id}
                    className="w-full h-10"
                    style={{ backgroundColor: `#${color3}` }}
                  ></Link>
                  <Link
                    href={`/palette/` + id}
                    className="w-full h-10 rounded-bl-xl rounded-br-xl"
                    style={{ backgroundColor: `#${color4}` }}
                  ></Link>
                  <div className="w-full flex justify-between items-center py-3">
                    <InsertLikes
                      likes_count={
                        Array.isArray(likes_count)
                          ? likes_count.length
                          : likes_count
                      }
                      id={color1 + color2 + color3 + color4}
                      color1={color1}
                      color2={color2}
                      color3={color3}
                      color4={color4}
                    />
                    <h4 className="text-xs font-normal opacity-80">
                      {dayjs(created_at).locale("ar").fromNow()}15
                    </h4>
                  </div>
                </div>
              )
            )}
          </div>
        </div>
      </section>
    );
  }

  const Dataa = await getDataOnePalette(slug);
  // دالة لتوزيع النتائج عشوائيًا

  // دالة لاختيار عنصر عشوائي من المصفوفة
  function getRandomElement<T>(array: T[]): T | undefined {
    if (!array || array.length === 0) return undefined; // التحقق من وجود بيانات
    const randomIndex = Math.floor(Math.random() * array.length);
    return array[randomIndex];
  }

  // التحقق واختيار عنصر عشوائي
  let randomTag: any;
  if (Dataa?.tags && Array.isArray(Dataa.tags)) {
    randomTag = getRandomElement(Dataa.tags);
    if (randomTag) {
      console.log("Random Tag:", randomTag); // عرض العنصر العشوائي
    } else {
      console.warn("Tags array is empty.");
    }
  } else {
    console.error("Invalid or missing tags data.");
  }

  const Data = await getDataSingleTag(`${randomTag}`);

  return (
    <section className="w-full">
      <div className="w-full h-full flex justify-center items-center">
        <div className="w-full flex flex-col justify-center items-center px-16 pt-7 max-w-[72vh]">
          <div
            className={`w-full h-56 rounded-tl-xl rounded-tr-xl`}
            style={{ backgroundColor: `#${Dataa?.color1}` }}
          ></div>
          <div
            className={`w-full h-32`}
            style={{ backgroundColor: `#${Dataa?.color2}` }}
          ></div>
          <div
            className={`w-full h-20`}
            style={{ backgroundColor: `#${Dataa?.color3}` }}
          ></div>
          <div
            className={`w-full h-20 rounded-bl-xl rounded-br-xl`}
            style={{ backgroundColor: `#${Dataa?.color4}` }}
          ></div>
          <div className="w-full flex justify-between items-center py-4">
            <div className="flex gap-3">
              <InsertLikes
                likes_count={
                  Array.isArray(Dataa?.likes_count)
                    ? Dataa?.likes_count.length
                    : Dataa?.likes_count
                }
                id={
                  Dataa?.color1 + Dataa?.color2 + Dataa?.color3 + Dataa?.color4
                }
                color1={Dataa?.color1}
                color2={Dataa?.color2}
                color3={Dataa?.color3}
                color4={Dataa?.color4}
              />
              <Button variant={"outline"} size={"default"}>
                Image
              </Button>
              <Button variant={"outline"} size={"default"}>
                <CopyToClipboardLink
                  link={`https://colorhunt.co/palette/${
                    Dataa?.color1 +
                    Dataa?.color2 +
                    Dataa?.color3 +
                    Dataa?.color4
                  }`}
                  display={`Link`}
                />
              </Button>
            </div>
            <h4 className="text-sm font-normal opacity-80">
              {dayjs(Dataa?.created_at).locale("en").fromNow()}
            </h4>
          </div>
        </div>
      </div>

      <div className="w-full h-full flex flex-col justify-center items-center my-10">
        <div className="w-4/5 flex justify-center items-center gap-3 text-sm">
          {[Dataa?.color1, Dataa?.color2, Dataa?.color3, Dataa?.color4].map(
            (color, index) => (
              <div
                key={index}
                className="w-full flex flex-col justify-center items-center gap-4"
              >
                <div
                  className="w-10 h-10 rounded-full"
                  style={{ backgroundColor: `#${color}` }}
                ></div>
                <div className="w-full line"></div>
                <span className="text-base hover:bg-neutral-100 px-2 py-1 rounded-xl duration-300">
                  <CopyToClipboardHex color={`${color}`} />
                </span>
                <div className="w-full line"></div>
                <CopyToClipboardHex color={`${hexToRgb(color)}`} />
              </div>
            )
          )}
        </div>
      </div>

      <div className="w-full flex justify-center items-center gap-3 my-16">
        {Dataa.tags?.map((tag: string, index: number) => (
          <Link
            href={`/palette/` + tag}
            key={index}
            className="border p-1 px-3 rounded-full flex justify-center items-center gap-2"
          >
            {colorsName.includes(tag) ? (
              <div
                className="w-4 h-4 rounded-full"
                style={{ backgroundColor: tag }}
              ></div>
            ) : null}
            <p>{tag}</p>
          </Link>
        ))}
      </div>
      <div className="w-full line"></div>

      <div className={`flex justify-center items-center gap-5 text-2xl my-8`}>
        <h1>more</h1>
        <span
          className={`border bg-stone-100 p-1 px-5 rounded-full font-medium`}
        >
          {randomTag}
        </span>
        <h1>Palettes</h1>
      </div>
      <div className="w-full h-full">
        <div className="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 animate-out gap-5">
          {Data?.map(
            ({
              id,
              color1,
              color2,
              color3,
              color4,
              created_at,
              likes_count,
            }: any) => (
              <div
                key={id}
                className={`flex flex-col justify-center items-center`}
              >
                <Link
                  href={`/palette/` + id}
                  className="w-full h-20 rounded-tl-xl rounded-tr-xl"
                  style={{ backgroundColor: `#${color1}` }}
                ></Link>
                <Link
                  href={`/palette/` + id}
                  className="w-full h-14"
                  style={{ backgroundColor: `#${color2}` }}
                ></Link>
                <Link
                  href={`/palette/` + id}
                  className="w-full h-10"
                  style={{ backgroundColor: `#${color3}` }}
                ></Link>
                <Link
                  href={`/palette/` + id}
                  className="w-full h-10 rounded-bl-xl rounded-br-xl"
                  style={{ backgroundColor: `#${color4}` }}
                ></Link>
                <div className="w-full flex justify-between items-center py-3">
                  <InsertLikes
                    likes_count={
                      Array.isArray(likes_count)
                        ? likes_count.length
                        : likes_count
                    }
                    id={color1 + color2 + color3 + color4}
                    color1={color1}
                    color2={color2}
                    color3={color3}
                    color4={color4}
                  />
                  <h4 className="text-xs font-normal opacity-80">
                    {dayjs(created_at).locale("ar").fromNow()}
                  </h4>
                </div>
              </div>
            )
          )}
        </div>
      </div>
    </section>
  );
}
