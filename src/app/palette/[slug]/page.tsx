/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable @typescript-eslint/no-explicit-any */
import { Button } from "@/components/ui/button";
import { sql } from "@vercel/postgres";
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

// Add support for relative time comparisons
dayjs.extend(relativeTime);

import type { Metadata, ResolvingMetadata } from "next";

type Props = {
  params: Promise<{ id: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
};

export async function generateMetadata(
  { params, searchParams }: Props,
  parent: ResolvingMetadata
): Promise<Metadata> {
  // read route params
  const slug = (await params).id;

  return {
    title: slug,
    description: `Color Palette: #${slug}`,

    // Add other metadata properties here


  };
}

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

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const slug = (await params).slug;

  const colorsName = [`red`, `green`, `blue`, `cyan`, `yellow`];

  // تحقق من طول الـ slug للتأكد أنه يتوافق مع الحد الأدنى
  if (slug.length <= 10) {
    // استعلام يجلب بيانات المجموعات التي تحتوي على الـ slug ضمن `tags`
    const { rows: tagg } = await sql`
  SELECT 
    cp.id, cp.color1, cp.color2, cp.color3, cp.color4, cp.created_at, 
    COALESCE(l.likes_count, 0) AS likes_count
  FROM color_palettes cp
  LEFT JOIN likes l ON cp.id = l.id  
  WHERE ${slug} = ANY(cp.tags)
    `;
    if (tagg.length === 0) {
      return <NotFound />;
    }
    return (
      <section className="w-full flex flex-col justify-center items-center">
        <div className="w-full h-full">
          <div className="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 animate-out gap-5">
            {tagg.map(
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
                      id={color1 + color2 + color3 + color4}
                      likes_count={`${likes_count}`}
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

  const { rows } = await sql`
    WITH palette_data AS (
      SELECT * FROM color_palettes WHERE id = ${slug}
    ),
    like_data AS (
      SELECT likes_count FROM likes WHERE id = ${slug}
    ),
    tagged_palettes AS (
      SELECT * FROM color_palettes WHERE ${slug} = ANY(tags)
    )
    SELECT 
      pd.color1, pd.color2, pd.color3, pd.color4, pd.created_at, pd.tags, 
      ld.likes_count
      
    FROM palette_data pd
    LEFT JOIN like_data ld ON pd.id = ${slug}
    LEFT JOIN tagged_palettes tp ON TRUE
  `;

  const palette = rows[0]; // Assuming there's at least one row
  const { likes_count, color1, color2, color3, color4, created_at, tags } =
    palette;

  // دالة لتوزيع النتائج عشوائيًا
  function shuffleArray(array: any[]) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  // ترتيب النتائج عشوائياً
  const shuffledTaggs = shuffleArray(tags);

  const { rows: taggs } = await sql`
  SELECT 
    cp.id, cp.color1, cp.color2, cp.color3, cp.color4, cp.created_at, 
    COALESCE(l.likes_count, 0) AS likes_count
  FROM color_palettes cp
  LEFT JOIN likes l ON cp.id = l.id  
  WHERE ${shuffledTaggs[0]} = ANY(cp.tags)
    `;

  const distance = dayjs(created_at).locale("en").fromNow();

  return (
    <section className="w-full">
      <div className="w-full h-full flex justify-center items-center">
        <div className="w-full flex flex-col justify-center items-center px-16 pt-7 max-w-[72vh]">
          <div
            className={`w-full h-56 rounded-tl-xl rounded-tr-xl`}
            style={{ backgroundColor: `#${color1}` }}
          ></div>
          <div
            className={`w-full h-32`}
            style={{ backgroundColor: `#${color2}` }}
          ></div>
          <div
            className={`w-full h-20`}
            style={{ backgroundColor: `#${color3}` }}
          ></div>
          <div
            className={`w-full h-20 rounded-bl-xl rounded-br-xl`}
            style={{ backgroundColor: `#${color4}` }}
          ></div>
          <div className="w-full flex justify-between items-center py-4">
            <div className="flex gap-3">
              <InsertLikes
                likes_count={
                  Array.isArray(likes_count) ? likes_count.length : likes_count
                }
                id={color1 + color2 + color3 + color4}
                color1={color1}
                color2={color2}
                color3={color3}
                color4={color4}
              />
              <Button variant={"outline"} size={"default"}>
                Image
              </Button>
              <Button variant={"outline"} size={"default"}>
                <CopyToClipboardLink
                  link={`https://colorhunt.co/palette/${
                    color1 + color2 + color3 + color4
                  }`}
                  display={`Link`}
                />
              </Button>
            </div>
            <h4 className="text-sm font-normal opacity-80">{distance}</h4>
          </div>
        </div>
      </div>

      <div className="w-full h-full flex flex-col justify-center items-center my-10">
        <div className="w-4/5 flex justify-center items-center gap-3 text-sm">
          {[color1, color2, color3, color4].map((color, index) => (
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
          ))}
        </div>
      </div>

      <div className="w-full flex justify-center items-center gap-3 my-16">
        {tags.map((tag: string, index: number) => (
          <Link
            href={`/palette/` + tag}
            key={index}
            className="border p-1 px-3 rounded-full flex justify-center items-center gap-2"
          >
            {colorsName.includes(tag) ? ( // تحقق مما إذا كان tag في قائمة الألوان
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
          {shuffledTaggs[0]}
        </span>
        <h1>Palettes</h1>
      </div>
      <div className="w-full h-full">
        <div className="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 animate-out gap-5">
          {taggs.map(
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
                    id={color1 + color2 + color3 + color4}
                    likes_count={`${likes_count}`}
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
